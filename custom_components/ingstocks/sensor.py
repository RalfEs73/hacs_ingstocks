import requests
import voluptuous as vol
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv
from .const import DOMAIN, DEFAULT_NAME

CONF_ISIN = "isin"

PLATFORM_SCHEMA = vol.Schema({
    vol.Required(CONF_ISIN): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    isin = config[CONF_ISIN]
    name = config.get(CONF_NAME)
    add_entities([StockSensor(name, isin)], True)

class StockSensor(SensorEntity):
    def __init__(self, name, isin):
        self._name = name
        self._isin = isin
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    def update(self):
        url = f"https://component-api.wertpapiere.ing.de/api/v1/components-ng/instrumentheader/{self._isin}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self._state = data.get("price")
            self._attributes = {
                "name": data.get("name"),
                "isin": data.get("isin"),
                "currency": data.get("currencySign"),
                "change_percent": data.get("changePercent"),
                "change_absolute": data.get("changeAbsolute"),
                "exchange": data.get("exchangeName"),
                "last_update": data.get("priceChangeDate"),
            }
        else:
            self._state = None