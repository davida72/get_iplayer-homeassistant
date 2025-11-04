# get_iplayer Downloader - Home Assistant Addon

Download BBC iPlayer shows using get_iplayer, optionally convert with ffmpeg, and save to your media folder.

## Features

- Download TV shows and radio programs from BBC iPlayer
- Optional audio/video conversion using ffmpeg
- Automatic file management and organization
- Copy files to Home Assistant media folder
- Fully configurable commands
- Support for all architectures

## Installation

### Method 1: Add Repository to Home Assistant

1. In Home Assistant, navigate to **Settings** → **Add-ons** → **Add-on Store**
2. Click the **three dots** (⋮) in the top right corner
3. Select **Repositories**
4. Add this URL: `https://github.com/davida72/get_iplayer-homeassistant`
5. Click **Add**
6. Find "get_iplayer Downloader" in the add-on store and click **Install**

### Method 2: Manual Installation

1. Navigate to your Home Assistant's `addons` directory
2. Clone this repository:
   ```bash
   cd /addons
   git clone https://github.com/davida72/get_iplayer-homeassistant.git
   ```
3. Restart Home Assistant
4. Navigate to **Settings** → **Add-ons** → **Add-on Store**
5. Find "get_iplayer Downloader" and click **Install**

## Configuration

### Basic Configuration

The addon comes with sensible defaults for downloading the latest BBC Newsround episode. Here's the default configuration:

```yaml
search_command: ""
download_command: "get_iplayer 'Newsround' --channel=CBBC --type=tv --get 1 --audio-only --output=/downloads --force --overwrite"
enable_ffmpeg: true
ffmpeg_command: "ffmpeg -i {input_file} -acodec mp3 -ab 128k {output_file}"
media_folder: "/media/downloads"
auto_delete_original: false
```

**Notes:**
- The program name must be in quotes and placed first for proper filtering
- `--get 1` downloads the first matching episode from search results
- `search_command` is empty by default (searching can take several minutes as it indexes all BBC programs)
- You can customize commands to download specific episodes or different programs

### Configuration Options

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| `search_command` | string | Command to search for episodes (optional, leave empty for faster execution) | `""` (empty) |
| `download_command` | string | Command to download episodes | `get_iplayer 'Newsround' --channel=CBBC --type=tv --get 1 --audio-only --output=/downloads --force --overwrite` |
| `enable_ffmpeg` | boolean | Enable ffmpeg conversion | `true` |
| `ffmpeg_command` | string | FFmpeg conversion command | `ffmpeg -i {input_file} -acodec mp3 -ab 128k {output_file}` |
| `media_folder` | string | Destination folder for files | `/media/downloads` |
| `auto_delete_original` | boolean | Delete original file after conversion | `false` |

### Command Placeholders

The following placeholders are automatically replaced by the addon:

- `{input_file}` - Path to input file (used in ffmpeg_command)
- `{output_file}` - Path to output file (used in ffmpeg_command)

## Usage Examples

### Example 1: Download Latest Newsround (Default - works out of the box!)

```yaml
search_command: ""
download_command: "get_iplayer 'Newsround' --channel=CBBC --type=tv --get 1 --audio-only --output=/downloads --force --overwrite"
enable_ffmpeg: true
ffmpeg_command: "ffmpeg -i {input_file} -acodec mp3 -ab 128k {output_file}"
media_folder: "/media/newsround"
auto_delete_original: true
```

### Example 2: Download Latest Doctor Who Episode (Full Video, No Conversion)

```yaml
search_command: ""
download_command: "get_iplayer 'Doctor Who' --type=tv --get 1 --output=/downloads --force --overwrite"
enable_ffmpeg: false
media_folder: "/media/tv_shows"
auto_delete_original: false
```

### Example 3: Download Latest Today Programme (Radio)

```yaml
search_command: ""
download_command: "get_iplayer 'Today Programme' --type=radio --get 1 --output=/downloads --force --overwrite"
enable_ffmpeg: true
ffmpeg_command: "ffmpeg -i {input_file} -acodec mp3 -ab 192k {output_file}"
media_folder: "/media/radio"
auto_delete_original: true
```

### Example 4: Download by PID (Programme ID)

```yaml
search_command: ""
download_command: "get_iplayer --pid=b006qykl --output=/downloads --force --overwrite"
enable_ffmpeg: false
media_folder: "/media/iplayer"
auto_delete_original: false
```

## get_iplayer Command Reference

### Common Options

- `--type=tv|radio` - Type of programme
- `--channel=<name>` - Filter by channel (e.g., BBC One, CBBC)
- `--get <index|pid>` - Download episode by index or PID
- `--pid=<pid>` - Download by Programme ID
- `--audio-only` - Download only audio stream
- `--output=<dir>` - Output directory
- `--force` - Force download
- `--overwrite` - Overwrite existing files
- `--quality=<quality>` - Video quality (e.g., hd, sd, web)

### Searching for Programmes

To find what to download, you can run the search command in the addon logs or use get_iplayer directly:

```bash
get_iplayer --type=tv "programme name"
```

This will show a list of available episodes with their index numbers.

## Automation

You can automate downloads using Home Assistant automations:

```yaml
automation:
  - alias: "Download Daily Newsround"
    trigger:
      platform: time
      at: "18:30:00"
    action:
      - service: hassio.addon_start
        data:
          addon: local_get-iplayer-downloader
```

## Troubleshooting

### Addon fails to start

- Check the addon logs for error messages
- Ensure your configuration is valid YAML
- Verify get_iplayer commands are correct

### No files downloaded

- Check if the programme is available on iPlayer
- Try searching with the search command first
- Verify episode index is correct

### Conversion fails

- Check ffmpeg command syntax
- Ensure input/output formats are compatible
- Check addon logs for ffmpeg errors

### Files not appearing in media folder

- Verify the media folder path is correct
- Check Home Assistant folder permissions
- Look in `/media` root if unsure of path

## Support

For issues, questions, or contributions:

- GitHub Issues: [https://github.com/davida72/get_iplayer-homeassistant/issues](https://github.com/davida72/get_iplayer-homeassistant/issues)
- get_iplayer Documentation: [https://github.com/get-iplayer/get_iplayer](https://github.com/get-iplayer/get_iplayer)

## Legal Notice

This addon is for personal use only. Ensure you comply with BBC's terms of service and only download content you have the right to access. The developers are not responsible for any misuse of this software.

## License

MIT License - See LICENSE file for details
