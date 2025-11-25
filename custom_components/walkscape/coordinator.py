"""DataUpdateCoordinator for WalkScape."""
from __future__ import annotations

from datetime import timedelta
import logging
from typing import Any

import aiohttp

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, API_BASE_URL, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class WalkScapeDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching WalkScape data."""

    def __init__(
        self,
        hass: HomeAssistant,
        session: aiohttp.ClientSession,
        character_id: str,
        scan_interval: int = SCAN_INTERVAL,
    ) -> None:
        """Initialize."""
        self.session = session
        self.character_id = character_id
        self.url = f"{API_BASE_URL}/{character_id}"

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=scan_interval),
        )

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from API."""
        try:
            async with self.session.get(
                self.url, timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                if response.status != 200:
                    raise UpdateFailed(f"Error fetching data: {response.status}")
                    
                data = await response.json()
                return data
                
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error communicating with API: {err}") from err
