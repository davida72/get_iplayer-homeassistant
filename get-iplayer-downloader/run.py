#!/usr/bin/env python3
"""
Home Assistant Addon for get_iplayer downloads
"""
import os
import sys
import json
import subprocess
import shutil
import glob
import time
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Paths
OPTIONS_FILE = '/data/options.json'
DOWNLOAD_DIR = '/downloads'
MEDIA_DIR = '/media'

def load_options():
    """Load addon configuration options"""
    try:
        with open(OPTIONS_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load options: {e}")
        sys.exit(1)

def run_command(command, shell=True, stream_output=False, allow_warning_codes=False):
    """Execute a shell command and return output

    Args:
        command: Command to execute
        shell: Use shell execution
        stream_output: Stream output line by line
        allow_warning_codes: If True, treat get_iplayer warning exit codes (like 29) as success
    """
    try:
        logger.info(f"Executing: {command}")

        if stream_output:
            # Stream output in real-time for long-running commands
            process = subprocess.Popen(
                command,
                shell=shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )

            output_lines = []
            for line in process.stdout:
                line = line.rstrip()
                if line:
                    logger.info(line)
                    output_lines.append(line)

            process.wait()

            # get_iplayer exit codes: 0=success, 29=success with warnings
            # Only raise error for actual failure codes
            if process.returncode != 0:
                if allow_warning_codes and process.returncode == 29:
                    logger.warning(f"Command completed with warnings (exit code {process.returncode})")
                else:
                    raise subprocess.CalledProcessError(process.returncode, command)

            return '\n'.join(output_lines), ''
        else:
            # Capture all output at once
            result = subprocess.run(
                command,
                shell=shell,
                capture_output=True,
                text=True,
                check=False  # Don't auto-raise on non-zero exit
            )

            if result.returncode != 0:
                if allow_warning_codes and result.returncode == 29:
                    logger.warning(f"Command completed with warnings (exit code {result.returncode})")
                else:
                    raise subprocess.CalledProcessError(result.returncode, command, result.stdout, result.stderr)

            logger.info(f"Output: {result.stdout}")
            return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed with exit code {e.returncode}")
        if hasattr(e, 'stdout') and e.stdout:
            logger.error(f"STDOUT: {e.stdout}")
        if hasattr(e, 'stderr') and e.stderr:
            logger.error(f"STDERR: {e.stderr}")
        raise

def search_episodes(search_command):
    """Search for episodes using get_iplayer"""
    logger.info("Searching for episodes...")
    stdout, stderr = run_command(search_command, allow_warning_codes=True)
    return stdout

def download_episode(download_command):
    """Download an episode using get_iplayer"""
    logger.info("Downloading episode...")
    stdout, stderr = run_command(download_command, stream_output=True, allow_warning_codes=True)
    return stdout

def convert_with_ffmpeg(input_file, output_file, ffmpeg_command):
    """Convert media file using ffmpeg"""
    logger.info(f"Converting {input_file} to {output_file}")

    # Replace placeholders in command
    command = ffmpeg_command.format(
        input_file=input_file,
        output_file=output_file
    )

    stdout, stderr = run_command(command, stream_output=True)
    return output_file

def copy_to_media(source_path, media_folder):
    """Copy file to media folder"""
    logger.info(f"Copying {source_path} to {media_folder}")

    # Ensure media folder exists
    os.makedirs(media_folder, exist_ok=True)

    # Get filename and copy
    filename = os.path.basename(source_path)
    destination = os.path.join(media_folder, filename)

    shutil.copy2(source_path, destination)
    logger.info(f"File copied to {destination}")
    return destination

def get_latest_file(directory, pattern="*"):
    """Get the most recently modified file in a directory"""
    files = glob.glob(os.path.join(directory, pattern))
    if not files:
        return None
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def main():
    """Main execution function"""
    logger.info("Starting get_iplayer Downloader addon...")

    # Load configuration
    options = load_options()
    logger.info(f"Loaded options: {json.dumps(options, indent=2)}")

    search_command = options.get('search_command')
    download_command = options.get('download_command')
    enable_ffmpeg = options.get('enable_ffmpeg', True)
    ffmpeg_command = options.get('ffmpeg_command')
    media_folder = options.get('media_folder', '/media/downloads')
    auto_delete_original = options.get('auto_delete_original', False)

    try:
        # Step 1: Search for episodes (optional - for user reference)
        if search_command:
            logger.info("=== Step 1: Searching for episodes ===")
            search_output = search_episodes(search_command)
            logger.info(search_output)

        # Step 2: Download episode
        logger.info("=== Step 2: Downloading episode ===")
        if not download_command:
            logger.error("No download command specified!")
            sys.exit(1)

        download_output = download_episode(download_command)

        # Find the downloaded file
        logger.info("Looking for downloaded file...")
        time.sleep(2)  # Give filesystem time to sync
        downloaded_file = get_latest_file(DOWNLOAD_DIR)

        if not downloaded_file:
            logger.error("No downloaded file found!")
            sys.exit(1)

        logger.info(f"Downloaded file: {downloaded_file}")
        file_to_copy = downloaded_file

        # Step 3: Convert with ffmpeg (optional)
        if enable_ffmpeg and ffmpeg_command:
            logger.info("=== Step 3: Converting with ffmpeg ===")

            # Determine output filename
            base_name = os.path.splitext(downloaded_file)[0]
            output_file = f"{base_name}.mp3"

            convert_with_ffmpeg(downloaded_file, output_file, ffmpeg_command)

            # Use converted file for copying
            file_to_copy = output_file

            # Delete original if requested
            if auto_delete_original and os.path.exists(downloaded_file):
                logger.info(f"Deleting original file: {downloaded_file}")
                os.remove(downloaded_file)
        else:
            logger.info("=== Step 3: Skipping ffmpeg conversion ===")

        # Step 4: Copy to media folder
        logger.info("=== Step 4: Copying to media folder ===")
        final_path = copy_to_media(file_to_copy, media_folder)

        logger.info("=== SUCCESS ===")
        logger.info(f"File available at: {final_path}")

    except Exception as e:
        logger.error(f"Error during execution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
