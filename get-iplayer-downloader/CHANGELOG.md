# Changelog

All notable changes to this project will be documented in this file.

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
