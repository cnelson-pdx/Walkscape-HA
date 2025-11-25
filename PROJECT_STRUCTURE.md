# Project Structure

This document explains the organization of the WalkScape Home Assistant integration.

## Directory Structure

```
walkscape-homeassistant/
├── .github/
│   └── workflows/
│       └── validate.yml          # GitHub Actions for CI/CD validation
├── custom_components/
│   └── walkscape/                # Main integration directory
│       ├── icons/                # Integration icons
│       │   └── ICON_INSTRUCTIONS.md
│       ├── translations/         # Localization files
│       │   └── en.json          # English translations
│       ├── __init__.py          # Integration setup and entry point
│       ├── config_flow.py       # GUI configuration flow
│       ├── const.py             # Constants and configuration
│       ├── coordinator.py       # Data update coordinator
│       ├── manifest.json        # Integration metadata
│       ├── sensor.py            # Sensor entity definitions
│       └── strings.json         # UI strings
├── .gitignore                   # Git ignore rules
├── hacs.json                    # HACS metadata
├── info.md                      # HACS store description
├── LICENSE                      # MIT License
├── LOVELACE_EXAMPLES.md         # Dashboard configuration examples
├── QUICK_START.md               # Quick setup checklist
├── README.md                    # Main documentation
└── SETUP_GUIDE.md               # Detailed setup instructions
```

## Core Files Explained

### Integration Files

#### `manifest.json`
Defines integration metadata for Home Assistant:
- Domain name (walkscape)
- Version information
- Dependencies
- Documentation links
- HACS requirements

#### `__init__.py`
Main entry point that:
- Sets up the integration
- Initializes the coordinator
- Registers sensor platform
- Handles integration loading/unloading

#### `config_flow.py`
Handles GUI configuration:
- User input form for character ID
- API validation
- Error handling
- Unique ID management

#### `const.py`
Central location for constants:
- Domain name
- API base URL
- Default scan interval (15 minutes)

#### `coordinator.py`
Manages data fetching:
- Periodic API polling
- Error handling
- Data updates to all sensors
- Caching and optimization

#### `sensor.py`
Defines all sensor entities:
- 16 different sensors for various stats
- Entity descriptions with icons
- Device information
- State classes for history tracking

### Configuration Files

#### `strings.json` and `translations/en.json`
UI text for:
- Configuration form labels
- Error messages
- Success messages
- Help text

### Documentation Files

#### `README.md`
Main documentation with:
- Overview and features
- Installation instructions
- Basic usage examples
- Support information

#### `SETUP_GUIDE.md`
Step-by-step setup guide:
- Detailed installation steps
- Configuration walkthrough
- Troubleshooting section
- Advanced configuration

#### `LOVELACE_EXAMPLES.md`
Dashboard examples:
- Various card configurations
- Complete dashboard layouts
- Custom card integration
- Best practices

#### `QUICK_START.md`
Quick reference checklist for setup

### Repository Files

#### `hacs.json`
HACS-specific configuration:
- Integration name
- Supported domains
- Minimum Home Assistant version

#### `info.md`
Short description for HACS store listing

#### `.github/workflows/validate.yml`
Automated validation:
- HACS validation
- Hassfest validation (Home Assistant)
- Runs on push and pull requests

## How It Works

### 1. Installation
- User installs through HACS
- Files copied to `custom_components/walkscape/`
- Home Assistant restart required

### 2. Configuration
- User adds integration via GUI
- `config_flow.py` handles input
- Validates character ID with API
- Creates config entry

### 3. Initialization
- `__init__.py` loads on startup
- Creates `WalkScapeDataUpdateCoordinator`
- Sets up sensor platform
- First data fetch occurs

### 4. Operation
- Coordinator polls API every 15 minutes
- Updates all sensors with new data
- Sensors maintain history
- Data available for automations and dashboards

### 5. Updates
- HACS checks for new versions
- User updates through HACS
- Restart applies changes

## Sensor Categories

### General Stats (6 sensors)
- Character Name
- Profile ID
- Total Steps
- Total XP
- Total Level
- Achievement Points

### Skill XP (10 sensors)
- Agility
- Carpentry
- Cooking
- Crafting
- Fishing
- Foraging
- Mining
- Smithing
- Trinketry
- Woodcutting

## Data Flow

```
WalkScape API
      ↓
Coordinator (polls every 15 min)
      ↓
Updates sensor states
      ↓
Available in Home Assistant
      ↓
Used in dashboards/automations
```

## Customization Points

### Change Update Interval
Edit `const.py`:
```python
SCAN_INTERVAL = 900  # seconds (default: 15 minutes)
```

### Add New Sensors
1. Add to `SENSOR_TYPES` in `sensor.py`
2. Define `WalkScapeSensorEntityDescription`
3. Provide `value_fn` to extract data

### Add Custom Icons
Place in `custom_components/walkscape/icons/`:
- `icon.png` (256x256)
- `icon@2x.png` (512x512)

### Modify API Endpoint
Edit `const.py`:
```python
API_BASE_URL = "https://api.web.walkscape.app/portal/shared/characters"
```

## Development Workflow

### Testing Locally
1. Copy `custom_components/walkscape/` to HA config
2. Restart Home Assistant
3. Add integration
4. Check logs for errors

### Making Changes
1. Edit files in `custom_components/walkscape/`
2. Restart Home Assistant
3. Test functionality
4. Commit changes

### Publishing Updates
1. Update version in `manifest.json`
2. Create GitHub release with version tag
3. HACS detects new version
4. Users notified of update

## File Sizes

Approximate sizes:
- Total integration: ~30 KB
- Core Python files: ~20 KB
- Documentation: ~50 KB
- Metadata files: ~5 KB

## Dependencies

### Required
- Home Assistant 2024.1.0 or newer
- Python 3.11+
- aiohttp (included in HA)

### Optional
- HACS (for easy installation)
- Custom Lovelace cards (for enhanced dashboards)

## Maintenance

### Regular Tasks
- Monitor GitHub issues
- Update dependencies if needed
- Test with new HA versions
- Improve documentation

### Version Updates
1. Increment version in `manifest.json`
2. Update README if needed
3. Create release notes
4. Tag release in GitHub

## Contributing

To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

See the main README for more details.

## Support

- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Community**: Home Assistant forums
- **Chat**: Home Assistant Discord

## License

This project is licensed under the MIT License - see LICENSE file.
