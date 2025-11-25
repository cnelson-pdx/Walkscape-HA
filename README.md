# WalkScape Home Assistant Integration

![Version](https://img.shields.io/badge/version-2025.11.2-blue)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2024.1.0+-green)
![HACS](https://img.shields.io/badge/HACS-Compatible-orange)

A custom Home Assistant integration for tracking your WalkScape character statistics.

![WalkScape](https://raw.githubusercontent.com/cnelson-pdx/Walkscape-HA/main/images/walkscape_logo.png)

## Features

- Track your character's total steps, XP, and level
- Monitor skill XP across all skills (Agility, Carpentry, Cooking, Crafting, Fishing, Foraging, Mining, Smithing, Trinketry, Woodcutting)
- View achievement points
- Automatic updates every 15 minutes
- Easy GUI configuration

## Installation

### HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add the repository URL: `https://github.com/cnelson-pdx/Walkscape-HA`
6. Select category: "Integration"
7. Click "Add"
8. Click "Install" on the WalkScape card
9. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/walkscape` folder to your Home Assistant's `custom_components` directory
2. Restart Home Assistant

## Configuration

1. Go to Settings → Devices & Services
2. Click "+ Add Integration"
3. Search for "WalkScape"
4. Enter your character ID from your WalkScape shared profile URL

### Finding Your Character ID

Your character ID is the last part of your shared profile URL. For example:
```
https://api.web.walkscape.app/portal/shared/characters/sykotic-91f66c1e-08d5-4d94-a07a-5b685a45e68a
```
The character ID would be: `sykotic-91f66c1e-08d5-4d94-a07a-5b685a45e68a`

## Available Sensors

The integration creates the following sensors:

### General Stats
- `sensor.walkscape_character_name` - Your character's name
- `sensor.walkscape_profile` - Your profile ID
- `sensor.walkscape_total_steps` - Total steps taken
- `sensor.walkscape_total_xp` - Total experience points
- `sensor.walkscape_total_level` - Combined level across all skills
- `sensor.walkscape_achievement_points` - Total achievement points

### Skill XP
- `sensor.walkscape_xp_agility`
- `sensor.walkscape_xp_carpentry`
- `sensor.walkscape_xp_cooking`
- `sensor.walkscape_xp_crafting`
- `sensor.walkscape_xp_fishing`
- `sensor.walkscape_xp_foraging`
- `sensor.walkscape_xp_mining`
- `sensor.walkscape_xp_smithing`
- `sensor.walkscape_xp_trinketry`
- `sensor.walkscape_xp_woodcutting`

## Usage Examples

### Lovelace Card Example

```yaml
type: entities
title: WalkScape Stats
entities:
  - entity: sensor.walkscape_character_name
  - entity: sensor.walkscape_total_steps
  - entity: sensor.walkscape_total_level
  - entity: sensor.walkscape_total_xp
  - entity: sensor.walkscape_achievement_points
```

### Automation Example

```yaml
automation:
  - alias: "Notify on Achievement Milestone"
    trigger:
      - platform: state
        entity_id: sensor.walkscape_achievement_points
    condition:
      - condition: template
        value_template: "{{ trigger.to_state.state | int % 100 == 0 }}"
    action:
      - service: notify.mobile_app
        data:
          message: "Congratulations! You've reached {{ states('sensor.walkscape_achievement_points') }} achievement points!"
```

## Support

For issues, feature requests, or questions, please open an issue on the [GitHub repository](https://github.com/cnelson-pdx/Walkscape-HA/issues).

## Credits

- [WalkScape](https://walkscape.app/) - The amazing game that makes walking fun!
- Home Assistant Community

## License

This project is licensed under the MIT License - see the LICENSE file for details.
