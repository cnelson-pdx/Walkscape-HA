# Icon Setup Instructions

To add a custom WalkScape icon to your integration:

## Option 1: Use WalkScape Logo (Recommended)

1. Download the official WalkScape logo
2. Resize it to 256x256 pixels
3. Save as `icon.png` in this directory
4. Save as `icon@2x.png` at 512x512 pixels for high-DPI displays

## Option 2: Create Your Own

Create a simple icon that represents WalkScape:
- Use a footprint or walking figure
- Include game elements like a compass or path
- Keep it simple and recognizable at small sizes
- Use the WalkScape color scheme

## File Requirements

- Format: PNG with transparency
- Size: 256x256 pixels (icon.png)
- Optional: 512x512 pixels (icon@2x.png) for retina displays
- Place in: `custom_components/walkscape/icons/`

## Integration Logo for GitHub

For the GitHub repository, also add:
- A larger logo (800x400 or similar) as `images/walkscape_logo.png`
- This will show up in the README

## Alternative: Use Home Assistant Icons

If you don't have a custom icon, the integration will fall back to using Material Design Icons (mdi) which are already included. The sensors already have appropriate icons assigned:
- Walk icon for steps
- Star icon for XP
- Trophy icon for levels
- Skill-specific icons for each skill
