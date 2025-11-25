"""Sensor platform for WalkScape."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import WalkScapeDataUpdateCoordinator


@dataclass
class WalkScapeSensorEntityDescription(SensorEntityDescription):
    """Describes WalkScape sensor entity."""

    value_fn: Callable[[dict[str, Any]], Any] | None = None


SENSOR_TYPES: tuple[WalkScapeSensorEntityDescription, ...] = (
    WalkScapeSensorEntityDescription(
        key="character_name",
        name="Character Name",
        icon="mdi:account",
        value_fn=lambda data: data.get("character_name"),
    ),
    WalkScapeSensorEntityDescription(
        key="profile",
        name="Profile",
        icon="mdi:card-account-details",
        value_fn=lambda data: data.get("id"),
    ),
    WalkScapeSensorEntityDescription(
        key="total_steps",
        name="Total Steps",
        icon="mdi:walk",
        native_unit_of_measurement="steps",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("total_steps"),
    ),
    WalkScapeSensorEntityDescription(
        key="total_xp",
        name="Total XP",
        icon="mdi:star",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("total_xp"),
    ),
    WalkScapeSensorEntityDescription(
        key="total_level",
        name="Total Level",
        icon="mdi:trophy",
        native_unit_of_measurement="level",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.get("statistics", {}).get("total_level"),
    ),
    WalkScapeSensorEntityDescription(
        key="achievement_points",
        name="Achievement Points",
        icon="mdi:medal",
        native_unit_of_measurement="pts",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("achievement_points"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_agility",
        name="XP Agility",
        icon="mdi:run",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("agility"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_carpentry",
        name="XP Carpentry",
        icon="mdi:hammer",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("carpentry"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_cooking",
        name="XP Cooking",
        icon="mdi:chef-hat",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("cooking"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_crafting",
        name="XP Crafting",
        icon="mdi:tools",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("crafting"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_fishing",
        name="XP Fishing",
        icon="mdi:fish",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("fishing"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_foraging",
        name="XP Foraging",
        icon="mdi:leaf",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("foraging"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_mining",
        name="XP Mining",
        icon="mdi:pickaxe",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("mining"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_smithing",
        name="XP Smithing",
        icon="mdi:anvil",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("smithing"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_trinketry",
        name="XP Trinketry",
        icon="mdi:diamond-stone",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("trinketry"),
    ),
    WalkScapeSensorEntityDescription(
        key="xp_woodcutting",
        name="XP Woodcutting",
        icon="mdi:axe",
        native_unit_of_measurement="xp",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: data.get("statistics", {}).get("woodcutting"),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up WalkScape sensors based on a config entry."""
    coordinator: WalkScapeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        WalkScapeSensor(coordinator, description, entry)
        for description in SENSOR_TYPES
    )


class WalkScapeSensor(CoordinatorEntity[WalkScapeDataUpdateCoordinator], SensorEntity):
    """Representation of a WalkScape sensor."""

    entity_description: WalkScapeSensorEntityDescription
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: WalkScapeDataUpdateCoordinator,
        description: WalkScapeSensorEntityDescription,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{entry.entry_id}_{description.key}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "name": f"WalkScape - {coordinator.data.get('character_name', 'Character')}",
            "manufacturer": "WalkScape",
            "model": "Character Stats",
            "entry_type": "service",
        }

    @property
    def native_value(self) -> Any:
        """Return the state of the sensor."""
        if self.entity_description.value_fn is None:
            return None
        return self.entity_description.value_fn(self.coordinator.data)
