# Changelog

All notable changes to this project will be documented in this file.

## [1.0.15] - 2025-11-04

### Changed
- Shortened description to "BBC iPlayer downloader with ffmpeg conversion" for better display in Home Assistant UI
- Enhanced automation examples with real-world use case showing download, delay, and playback
- Added detailed notes for automation configuration including addon slug and media player setup

## [1.0.14] - 2025-11-04

### Fixed
- **Critical fix**: Added `--limit-matches 1` to prevent processing all matching episodes
- Previously `--get` would attempt to download all 30+ matching episodes (only first succeeded, rest failed)
- Now correctly limits search results to just 1 episode (the latest) before downloading
- Dramatically reduces execution time and eliminates unnecessary warnings

## [1.0.13] - 2025-11-04

### Fixed
- **Critical fix**: Changed `--get 1` to just `--get`
- `--get 1` was downloading cache index #1 (Welsh show) instead of first search result
- Now correctly downloads only the first matching episode from search results
- No more unwanted extra downloads

## [1.0.12] - 2025-11-04

### Fixed
- **Critical fix**: Changed `--reverse` to `--sortreverse` - correct get_iplayer syntax
- `--reverse` is not a valid get_iplayer option and was causing downloads to fail
- Changed `--sort=firstbcast` to `--sort=available` for more reliable sorting
- Downloads now work correctly with proper sorting to get latest episode

## [1.0.11] - 2025-11-04

### Changed
- Improved documentation table formatting for better readability in dark mode
- Simplified Configuration Options table with shorter descriptions
- Moved detailed defaults and descriptions to "Option Details" section below table
- Made option names bold for better visibility

## [1.0.10] - 2025-11-04

### Fixed
- **Always get the latest episode** - Added `--sort=firstbcast --reverse` to guarantee newest episode
- Previously `--get 1` would get first result which might not be the newest
- Now sorts by first broadcast date in reverse order before getting first result

### Changed
- Renamed "Final Filename" to "Final Filename (optional)" to make it clearer it's not required
- Updated all documentation and examples with sorting flags

## [1.0.9] - 2025-11-04

### Added
- **Final Filename option** - specify a custom filename for the output file (e.g., `newsround_latest.mp3`)
- Perfect for daily automation - always save to the same filename so you can play "the latest" each day
- Extension is optional - will use the current file extension if not specified
- Leave empty to keep the original downloaded filename

### Changed
- **Configuration options now have human-readable names:**
  - `download_command` → `Download Command`
  - `enable_ffmpeg` → `Convert Audio`
  - `ffmpeg_command` → `Conversion Command`
  - `media_folder` → `Output Folder`
  - `auto_delete_original` → `Delete Original After Conversion`
- **Removed `search_command` option** - not needed with `--since` flag
- Replaced `--sort=available --reverse` with `--since 168` (last 7 days)
- Much faster execution - only indexes programmes from the last week instead of all 8000+ BBC programmes
- Simpler command structure
- First matching result is naturally the most recent with --since
- Removed unused search step from execution flow
- Execution now has 4 steps (added rename step between conversion and copy)

## [1.0.8] - 2025-11-04

### Fixed
- Added `--sort=available --reverse` to download the most recent available episode
- Prevents trying to download expired episodes (BBC typically keeps shows for 30 days)
- Now gets the newest episode first instead of oldest
- Fixes issue where older unavailable episodes were being attempted first

## [1.0.7] - 2025-11-04

### Fixed
- Fixed download_command to properly search for Newsround specifically
- Program name now in quotes and placed first in command
- Previously was downloading first program from entire cache instead of first Newsround
- Changed from `--get 1 --type=tv --channel=CBBC Newsround` to `'Newsround' --channel=CBBC --type=tv --get 1`

## [1.0.6] - 2025-11-04

### Fixed
- Handle get_iplayer exit code 29 (success with warnings) properly
- Addon now continues processing even when AtomicParsley warning occurs
- Downloads complete successfully despite non-critical warnings
- Added allow_warning_codes parameter to treat code 29 as success

## [1.0.5] - 2025-11-04

### Fixed
- Stream output in real-time for download and conversion commands
- Users can now see progress instead of addon appearing to hang
- Added stream_output parameter to run_command function
- Download progress and ffmpeg conversion progress now visible in logs

## [1.0.4] - 2025-11-04

### Fixed
- Disabled search_command by default (was causing addon to hang)
- Search step can take several minutes as it indexes all BBC programs
- Addon now goes straight to download for faster execution
- Users can still enable search_command if needed for reference

## [1.0.3] - 2025-11-03

### Added
- Added custom logo/icon for the addon

## [1.0.2] - 2025-11-03

### Fixed
- Updated default download_command to actually work out of the box
- Changed from placeholder `{episode_index}` to `--get 1` with search criteria
- Now downloads the latest Newsround episode by default without configuration

## [1.0.1] - 2025-11-03

### Fixed
- Removed atomicparsley dependency (not available in Alpine 3.18)
- Docker build now completes successfully

## [1.0.0] - 2025-11-03

### Added
- Initial release
- get_iplayer integration for downloading BBC iPlayer content
- Configurable search and download commands
- Optional ffmpeg conversion support
- Automatic file copying to Home Assistant media folder
- Support for all Home Assistant architectures
- Comprehensive configuration options
- Example configurations for TV, radio, and audio downloads
