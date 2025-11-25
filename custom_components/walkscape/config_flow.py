"""Config flow for WalkScape integration."""
from __future__ import annotations

import logging
from typing import Any

import aiohttp
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN, API_BASE_URL

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("character_id"): str,
        vol.Optional("scan_interval", default=900): vol.All(
            vol.Coerce(int), vol.Range(min=300, max=3600)
        ),
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.
    
    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
    character_id = data["character_id"]
    url = f"{API_BASE_URL}/{character_id}"
    
    session = async_get_clientsession(hass)
    
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            if response.status == 404:
                raise InvalidCharacter
            if response.status != 200:
                raise CannotConnect
                
            json_data = await response.json()
            character_name = json_data.get("character_name", "Unknown")
            
    except aiohttp.ClientError as err:
        _LOGGER.error("Error connecting to WalkScape API: %s", err)
        raise CannotConnect from err
    except Exception as err:
        _LOGGER.exception("Unexpected exception: %s", err)
        raise CannotConnect from err

    return {"title": f"WalkScape - {character_name}", "character_name": character_name}


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for WalkScape."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidCharacter:
                errors["base"] = "invalid_character"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                await self.async_set_unique_id(user_input["character_id"])
                self._abort_if_unique_id_configured()
                
                return self.async_create_entry(
                    title=info["title"],
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
            description_placeholders={
                "character_id_example": "sykotic-91f66c1e-08d5-4d94-a07a-5b685a45e68a"
            },
        )

    @staticmethod
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidCharacter(HomeAssistantError):
    """Error to indicate the character ID is invalid."""


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for WalkScape."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        "scan_interval",
                        default=self.config_entry.options.get(
                            "scan_interval",
                            self.config_entry.data.get("scan_interval", 900),
                        ),
                    ): vol.All(vol.Coerce(int), vol.Range(min=300, max=3600)),
                }
            ),
        )
