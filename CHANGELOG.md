# Changelog

All notable changes to the WalkScape Home Assistant integration will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project uses [Calendar Versioning](https://calver.org/) with the format `YYYY.MM.RELEASE`.

## [Unreleased]

### Planned
- Service call for manual refresh
- Additional sensors based on community feedback
- Enhanced error handling and logging

## [2025.11.2] - 2025-11-25

### Fixed
- 🐛 Fixed missing scan_interval field in config flow
- 🐛 Fixed missing options flow handler for runtime configuration
- 🐛 Fixed coordinator not accepting custom scan_interval parameter
- 🐛 Fixed __init__.py not passing scan_interval to coordinator

### Technical
- Added OptionsFlowHandler class for runtime configuration
- Added async_get_options_flow method to ConfigFlow
- Added update listener for option changes
- Coordinator now properly accepts and uses scan_interval parameter

## [2025.11.1] - 2025-11-25

### Added
- 🎉 Initial public release
- ✨ GUI configuration flow for easy setup
- ✨ Configurable polling interval (300-3600 seconds)
- ✨ Options flow to change polling interval after setup
- 📊 16 sensors tracking WalkScape character stats:
  - Character name and profile ID
  - Total steps, XP, and level
  - Achievement points
  - Individual skill XP for all 10 skills (Agility, Carpentry, Cooking, Crafting, Fishing, Foraging, Mining, Smithing, Trinketry, Woodcutting)
- 🔄 Automatic data updates via DataUpdateCoordinator
- 🎯 Device integration with proper grouping
- 📱 HACS compatibility
- 🌐 Support for WalkScape shared profile API
- 🛡️ Input validation and error handling
- 🎨 Material Design Icons for all sensors
- 📚 Comprehensive documentation

### Features
- Character ID validation during setup
- API connectivity testing
- Unique ID management to prevent duplicates
- State classes for long-term statistics
- Proper entity naming and organization
- Support for multiple WalkScape characters (add integration multiple times)

### Technical
- Modern async/await architecture
- Type hints throughout codebase
- Follows Home Assistant integration best practices
- Clean separation of concerns
- Comprehensive error handling
- Automated GitHub Actions validation

### Documentation
- Complete README with installation instructions
- Detailed setup guide
- Lovelace dashboard examples
- Troubleshooting section
- Project structure documentation
- Developer guides

## Version History

### Versioning Scheme

This project uses Calendar Versioning (CalVer):
- Format: `YYYY.MM.RELEASE`
- Example: `2025.11.1` = First release in November 2025
- Release numbers reset each month

### Future Versions

**2025.11.x** - Bug fixes and minor improvements for November 2025 release
**2025.12.x** - December 2025 features and updates
**2026.01.x** - January 2026 features and updates

## Breaking Changes

None yet - this is the initial release!

Future breaking changes will be clearly documented here with migration guides.

## Deprecations

None yet!

## Security

No known security issues. Please report any security concerns to the issue tracker.

## Links

- [GitHub Repository](https://github.com/cnelson-pdx/Walkscape-HA)
- [Issue Tracker](https://github.com/cnelson-pdx/Walkscape-HA/issues)
- [WalkScape Official](https://walkscape.app/)
- [Home Assistant](https://www.home-assistant.io/)
- [HACS](https://hacs.xyz/)

---

## How to Read This Changelog

### Categories

- **Added** - New features
- **Changed** - Changes to existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Security updates

### Emojis

- 🎉 Major release
- ✨ New feature
- 🐛 Bug fix
- 📝 Documentation
- 🔧 Maintenance
- ⚡ Performance
- 🛡️ Security
- 💥 Breaking change

---

**Note:** Versions follow `YYYY.MM.RELEASE` format. See [VERSIONING_GUIDE.md](VERSIONING_GUIDE.md) for details.
