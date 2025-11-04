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
Download Command: "get_iplayer 'Newsround' --channel=CBBC --type=tv --since 168 --sort=firstbcast --reverse --get 1 --audio-only --output=/downloads --force --overwrite"
Convert Audio: true
Conversion Command: "ffmpeg -i {input_file} -acodec mp3 -ab 128k {output_file}"
Output Folder: "/media/downloads"
Final Filename (optional): ""
Delete Original After Conversion: false
```

**Notes:**
- The program name must be in quotes and placed first for proper filtering
- `--since 168` only caches programmes from the last 7 days (168 hours) - **much faster than full cache!**
- `--sort=firstbcast --reverse` ensures you always get the newest episode first
- `--get 1` downloads the first matching episode (which is now guaranteed to be the latest)
- You can customize commands to download specific episodes or different programs

### Configuration Options

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| Download Command | string | The get_iplayer command to download your chosen programme | `get_iplayer 'Newsround' --channel=CBBC --type=tv --since 168 --sort=firstbcast --reverse --get 1 --audio-only --output=/downloads --force --overwrite` |
| Convert Audio | boolean | Convert the downloaded file using ffmpeg | `true` |
| Conversion Command | string | The ffmpeg command for audio conversion | `ffmpeg -i {input_file} -acodec mp3 -ab 128k {output_file}` |
| Output Folder | string | Where to save the final file in Home Assistant | `/media/downloads` |
| Final Filename (optional) | string | Rename the file before copying (e.g., `newsround_latest.mp3`). Leave empty to keep original filename. Extension is optional - will use current file extension if not specified. | `""` (empty) |
| Delete Original After Conversion | boolean | Automatically delete the original file after conversion to save space | `false` |

### Command Placeholders

The following placeholders are automatically replaced by the addon:

- `{input_file}` - Path to input file (used in ffmpeg_command)
- `{output_file}` - Path to output file (used in ffmpeg_command)

## Usage Examples

### Example 1: Download Latest Newsround with Fixed Filename (Perfect for daily automation!)

```yaml
Download Command: "get_iplayer 'Newsround' --channel=CBBC --type=tv --since 168 --sort=firstbcast --reverse --get 1 --audio-only --output=/downloads --force --overwrite"
Convert Audio: true
Conversion Command: "ffmpeg -i {input_file} -acodec mp3 -ab 128k {output_file}"
Output Folder: "/media/newsround"
Final Filename (optional): "newsround_latest.mp3"
Delete Original After Conversion: true
```

This will always save the file as `newsround_latest.mp3`, so you can play the same filename every day and it will automatically be the latest episode!

### Example 2: Download Latest Doctor Who Episode (Full Video, No Conversion)

```yaml
Download Command: "get_iplayer 'Doctor Who' --type=tv --since 720 --sort=firstbcast --reverse --get 1 --output=/downloads --force --overwrite"
Convert Audio: false
Output Folder: "/media/tv_shows"
Final Filename (optional): ""
Delete Original After Conversion: false
```

### Example 3: Download Latest Today Programme (Radio)

```yaml
Download Command: "get_iplayer 'Today Programme' --type=radio --since 168 --sort=firstbcast --reverse --get 1 --output=/downloads --force --overwrite"
Convert Audio: true
Conversion Command: "ffmpeg -i {input_file} -acodec mp3 -ab 192k {output_file}"
Output Folder: "/media/radio"
Final Filename (optional): ""
Delete Original After Conversion: true
```

### Example 4: Download by PID (Programme ID)

```yaml
Download Command: "get_iplayer --pid=b006qykl --output=/downloads --force --overwrite"
Convert Audio: false
Output Folder: "/media/iplayer"
Final Filename (optional): ""
Delete Original After Conversion: false
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
