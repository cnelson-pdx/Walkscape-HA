# WalkScape Home Assistant Integration - Setup Guide

This guide will walk you through setting up the WalkScape integration for Home Assistant.

## Prerequisites

- Home Assistant installed and running
- HACS (Home Assistant Community Store) installed
- A WalkScape account with a shared profile

## Step 1: Get Your Character ID

1. Open the WalkScape app or web portal
2. Go to your character profile
3. Enable profile sharing if not already enabled
4. Copy your shared profile URL
5. Extract the character ID (the part after `/characters/`)

Example URL:
```
https://api.web.walkscape.app/portal/shared/characters/sykotic-91f66c1e-08d5-4d94-a07a-5b685a45e68a
```

Character ID:
```
sykotic-91f66c1e-08d5-4d94-a07a-5b685a45e68a
```

## Step 2: Install the Integration via HACS

### Add Custom Repository

1. Open Home Assistant
2. Go to **HACS** (in the sidebar)
3. Click on **Integrations**
4. Click the **three dots** menu in the top right
5. Select **Custom repositories**
6. Add this repository:
   - **URL**: `https://github.com/yourgithubusername/walkscape-homeassistant`
   - **Category**: Integration
7. Click **Add**

### Install the Integration

1. Search for "WalkScape" in HACS
2. Click on the WalkScape integration
3. Click **Download**
4. Select the latest version
5. Click **Download** again
6. **Restart Home Assistant** (required for the integration to load)

## Step 3: Configure the Integration

1. After restarting, go to **Settings** → **Devices & Services**
2. Click **+ Add Integration** (bottom right)
3. Search for "WalkScape"
4. Click on WalkScape when it appears
5. Enter your **Character ID** (from Step 1)
6. Click **Submit**

The integration will:
- Validate your character ID
- Fetch your character data
- Create all sensors
- Display as a device with your character name

## Step 4: Verify Installation

1. Go to **Settings** → **Devices & Services**
2. Find the WalkScape integration
3. Click on it to see all your sensors
4. Check that sensors are showing current values

### Available Sensors

You should see 16 sensors created:
- Character Name
- Profile ID
- Total Steps
- Total XP
- Total Level
- Achievement Points
- XP for each skill (10 skills)

## Step 5: Using Your Sensors

### View in Dashboard

Create a new card in your dashboard:

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

### Create Automations

Example - Celebrate milestones:

```yaml
automation:
  - alias: "WalkScape Level Milestone"
    trigger:
      - platform: state
        entity_id: sensor.walkscape_total_level
    condition:
      - condition: template
        value_template: "{{ trigger.to_state.state | int % 10 == 0 }}"
    action:
      - service: notify.mobile_app
        data:
          title: "WalkScape Achievement!"
          message: "You've reached level {{ states('sensor.walkscape_total_level') }}! 🎉"
```

### Statistics and History

All sensors with state_class will automatically track history:
- View long-term XP trends
- Track daily step progress
- Monitor skill progression over time

Go to **History** in Home Assistant and search for your WalkScape sensors.

## Troubleshooting

### Integration Not Showing Up

- Ensure you restarted Home Assistant after installation
- Check Home Assistant logs: **Settings** → **System** → **Logs**
- Look for errors related to "walkscape"

### "Cannot Connect" Error

- Verify your internet connection
- Check if the WalkScape API is accessible
- Test your shared profile URL in a browser

### "Invalid Character" Error

- Double-check your character ID
- Ensure profile sharing is enabled in WalkScape
- Verify the complete ID was copied (no spaces)

### Sensors Not Updating

- Default update interval is 15 minutes
- Force update: **Developer Tools** → **States** → Click sensor → **Update**
- Check if your shared profile is still active in WalkScape

### Removing the Integration

1. Go to **Settings** → **Devices & Services**
2. Find WalkScape integration
3. Click the three dots menu
4. Select **Delete**
5. Confirm deletion

All sensors will be removed automatically.

## Advanced Configuration

### Changing Update Interval

The default update interval is 15 minutes (900 seconds). To change this:

1. Edit `custom_components/walkscape/const.py`
2. Change `SCAN_INTERVAL = 900` to your desired seconds
3. Restart Home Assistant

**Note**: Too frequent updates may impact performance or exceed API limits.

### Multiple Characters

To track multiple characters:
1. Add the integration multiple times
2. Use a different character ID each time
3. Each character will appear as a separate device

## Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/yourgithubusername/walkscape-homeassistant/issues)
- **Home Assistant Community**: [Discuss in the forums](https://community.home-assistant.io/)
- **WalkScape Discord**: Get help with character IDs and profile sharing

## Updates

The integration will notify you of updates through HACS. To update:

1. Open HACS
2. Go to Integrations
3. Find WalkScape with an update badge
4. Click **Update**
5. Restart Home Assistant

## Next Steps

- Create custom dashboard cards
- Set up automations for achievements
- Track your progress with history graphs
- Share your setup with the community!

Enjoy tracking your WalkScape journey in Home Assistant! 🚶‍♂️✨
