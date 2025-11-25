# WalkScape Dashboard Examples

Here are some example Lovelace configurations for displaying your WalkScape data.

## Basic Stats Card

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

## Skills Overview

```yaml
type: entities
title: WalkScape Skills
entities:
  - entity: sensor.walkscape_xp_agility
  - entity: sensor.walkscape_xp_carpentry
  - entity: sensor.walkscape_xp_cooking
  - entity: sensor.walkscape_xp_crafting
  - entity: sensor.walkscape_xp_fishing
  - entity: sensor.walkscape_xp_foraging
  - entity: sensor.walkscape_xp_mining
  - entity: sensor.walkscape_xp_smithing
  - entity: sensor.walkscape_xp_trinketry
  - entity: sensor.walkscape_xp_woodcutting
```

## Compact Grid View

```yaml
type: grid
columns: 2
square: false
cards:
  - type: statistic
    entity: sensor.walkscape_total_steps
    name: Steps
    icon: mdi:walk
  - type: statistic
    entity: sensor.walkscape_total_level
    name: Total Level
    icon: mdi:trophy
  - type: statistic
    entity: sensor.walkscape_total_xp
    name: Total XP
    icon: mdi:star
  - type: statistic
    entity: sensor.walkscape_achievement_points
    name: Achievements
    icon: mdi:medal
```

## History Graph

```yaml
type: history-graph
title: WalkScape Progress
entities:
  - entity: sensor.walkscape_total_steps
  - entity: sensor.walkscape_total_xp
  - entity: sensor.walkscape_total_level
hours_to_show: 168
```

## Top Skills Card

```yaml
type: custom:bar-card
entities:
  - entity: sensor.walkscape_xp_agility
    name: Agility
  - entity: sensor.walkscape_xp_carpentry
    name: Carpentry
  - entity: sensor.walkscape_xp_cooking
    name: Cooking
  - entity: sensor.walkscape_xp_crafting
    name: Crafting
  - entity: sensor.walkscape_xp_fishing
    name: Fishing
  - entity: sensor.walkscape_xp_foraging
    name: Foraging
  - entity: sensor.walkscape_xp_mining
    name: Mining
  - entity: sensor.walkscape_xp_smithing
    name: Smithing
  - entity: sensor.walkscape_xp_trinketry
    name: Trinketry
  - entity: sensor.walkscape_xp_woodcutting
    name: Woodcutting
title: Skill Levels
max: 1000000
positions:
  icon: inside
  name: inside
  value: inside
height: 30px
```

Note: This requires the [Bar Card](https://github.com/custom-cards/bar-card) custom component.

## Gauge Card for Total Level

```yaml
type: gauge
entity: sensor.walkscape_total_level
name: Total Level
min: 0
max: 1000
needle: true
severity:
  green: 700
  yellow: 400
  red: 0
```

## Complete Dashboard View

```yaml
title: WalkScape
path: walkscape
icon: mdi:walk
cards:
  - type: vertical-stack
    cards:
      - type: markdown
        content: |
          # {{ states('sensor.walkscape_character_name') }}
          
      - type: grid
        columns: 3
        square: false
        cards:
          - type: statistic
            entity: sensor.walkscape_total_steps
            name: Steps
          - type: statistic
            entity: sensor.walkscape_total_level
            name: Level
          - type: statistic
            entity: sensor.walkscape_achievement_points
            name: Achievements
            
      - type: horizontal-stack
        cards:
          - type: gauge
            entity: sensor.walkscape_total_level
            name: Total Level
            min: 0
            max: 1000
            needle: true
            
      - type: entities
        title: Combat & Gathering Skills
        entities:
          - sensor.walkscape_xp_agility
          - sensor.walkscape_xp_fishing
          - sensor.walkscape_xp_foraging
          - sensor.walkscape_xp_mining
          - sensor.walkscape_xp_woodcutting
          
      - type: entities
        title: Crafting Skills
        entities:
          - sensor.walkscape_xp_carpentry
          - sensor.walkscape_xp_cooking
          - sensor.walkscape_xp_crafting
          - sensor.walkscape_xp_smithing
          - sensor.walkscape_xp_trinketry
          
      - type: history-graph
        title: XP Progress (7 days)
        entities:
          - sensor.walkscape_total_xp
        hours_to_show: 168
```

## Mobile-Friendly Compact View

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      ### {{ states('sensor.walkscape_character_name') }}
      
  - type: glance
    entities:
      - entity: sensor.walkscape_total_steps
        name: Steps
      - entity: sensor.walkscape_total_level
        name: Level
      - entity: sensor.walkscape_total_xp
        name: XP
        
  - type: button
    entity: sensor.walkscape_achievement_points
    name: Achievements
    icon: mdi:medal
    tap_action:
      action: more-info
```

## Markdown Card with Dynamic Content

```yaml
type: markdown
content: |
  # WalkScape Character: {{ states('sensor.walkscape_character_name') }}
  
  **Total Progress**
  - 🚶 Steps: {{ states('sensor.walkscape_total_steps') }}
  - ⭐ Total XP: {{ states('sensor.walkscape_total_xp') }}
  - 🏆 Total Level: {{ states('sensor.walkscape_total_level') }}
  - 🏅 Achievement Points: {{ states('sensor.walkscape_achievement_points') }}
  
  **Top Skills**
  {% set skills = [
    ('Agility', states('sensor.walkscape_xp_agility')),
    ('Carpentry', states('sensor.walkscape_xp_carpentry')),
    ('Cooking', states('sensor.walkscape_xp_cooking')),
    ('Crafting', states('sensor.walkscape_xp_crafting')),
    ('Fishing', states('sensor.walkscape_xp_fishing'))
  ] %}
  {% for skill, xp in skills %}
  - {{ skill }}: {{ xp }} XP
  {% endfor %}
```

## Conditional Card (Show when Level Up)

```yaml
type: conditional
conditions:
  - entity: sensor.walkscape_total_level
    state_not: "0"
card:
  type: markdown
  content: |
    ## 🎉 Congratulations!
    You've reached level {{ states('sensor.walkscape_total_level') }}!
```

## Custom Button Card

```yaml
type: custom:button-card
entity: sensor.walkscape_total_level
name: WalkScape Level
icon: mdi:trophy
show_state: true
styles:
  card:
    - background-color: var(--primary-color)
    - border-radius: 10px
  name:
    - color: white
  state:
    - color: white
    - font-size: 20px
    - font-weight: bold
tap_action:
  action: more-info
```

Note: This requires [Button Card](https://github.com/custom-cards/button-card).

## Tips for Dashboard Design

1. **Use Grid Layouts**: Organize cards in grids for better mobile responsiveness
2. **History Graphs**: Track long-term progress with 7-day or 30-day views
3. **Gauge Cards**: Great for visualizing levels and progress
4. **Conditional Cards**: Show special messages for milestones
5. **Custom Cards**: Enhance with HACS custom cards like Bar Card or Button Card
6. **Icons**: Use MDI icons to make your dashboard visually appealing
7. **Colors**: Use severity levels in gauges to show progress
