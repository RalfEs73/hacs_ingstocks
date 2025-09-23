# ING Stocks Home Assistant Integration

Mit dieser benutzerdefinierten Integration kannst du Aktienkurse von ING direkt als Sensor in Home Assistant einbinden.

## Features

- Abruf von Aktienkursen per REST-API (ING)
- Anzeige von Preis, Währung, Kursänderung und weiteren Attributen
- Unterstützung für mehrere Aktien (ISINs)
- Automatische Aktualisierung (z. B. alle 5 Minuten)
- Passendes Icon (`mdi:euro`) und device_class (`monetary`)

## Installation

Die empfohlene Methode ist die Installation über HACS.
[![Open your Home Assistant instance and open the ING Stocks custom component repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ralfes73&repository=hacs_ingstocks)

Starte Home Assistant neu.

## Konfiguration

Füge in deiner `configuration.yaml` folgenden Abschnitt hinzu:

```yaml
sensor:
  - platform: ingstocks
    isin: "DE000BASF111"
    name: "BASF Aktie" # Optional - Name überschreiben
	scan_interval: 300  # Optional - Alle 5 Minuten (300 Sekunden)
```