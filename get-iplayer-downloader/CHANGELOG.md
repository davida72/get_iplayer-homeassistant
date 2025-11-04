# Changelog

All notable changes to this project will be documented in this file.

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
