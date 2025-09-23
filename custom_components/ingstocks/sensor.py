import logging
import aiohttp
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

DOMAIN = "ingstocks"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    isin = config.get("isin")
    if not isin:
        _LOGGER.error("Keine ISIN angegeben!")
        return
    async_add_entities([INGStocksSensor(isin)], True)

class INGStocksSensor(Entity):
    def __init__(self, isin):
        self._isin = isin
        self._state = None
        self._attributes = {}

    @property
    def device_class(self):
        return "monetary"

    @property
    def unit_of_measurement(self):
        return "€"

    @property
    def icon(self):
        return "mdi:currency-eur"

    @property
    def name(self):
        return f"ING Stocks {self._isin}"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    async def async_update(self):
        url = f"https://component-api.wertpapiere.ing.de/api/v1/components-ng/instrumentheader/{self._isin}"
        _LOGGER.debug("Rufe API auf: %s", url)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    _LOGGER.debug("API Antwort: %s", data)
                    price = data.get("price")
                    if price is None:
                        _LOGGER.warning("Kein Preis für ISIN %s gefunden!", self._isin)
                        self._state = "unavailable"
                        return
                    self._state = round(price, 2)
                    self._attributes = {
                        "name": data.get("name"),
                        "isin": data.get("isin"),
                        "currency": data.get("currencySign"),
                        "change_percent": round(data.get("changePercent", 0), 2),
                        "change_absolute": data.get("changeAbsolute"),
                        "exchange": data.get("exchangeName"),
                        "last_update": data.get("priceChangeDate"),
                    }
        except Exception as e:
            _LOGGER.error("Fehler beim Abrufen der Aktie %s: %s", self._isin, e)
            self._state = "unavailable"
            self._attributes = {}
