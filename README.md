[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub release](https://img.shields.io/github/release/RalfEs73/hacs_ingstocks.svg)](https://github.com/RalfEs73/hacs_ingstocks/releases)

# ING Stocks Home Assistant Integration

Mit dieser benutzerdefinierten Integration kannst du Aktienkurse von ING direkt als Sensor in Home Assistant einbinden.

## Features

- Abruf von Aktienkursen über ING
- Anzeige von Preis, Währung, Kursänderung und weiteren Attributen
- Unterstützung für mehrere Aktien (ISINs)
- Automatische Aktualisierung (z. B. alle 5 Minuten)

## Installation

Die empfohlene Methode ist die Installation über HACS.

[![Open your Home Assistant instance and open the ING Stocks custom component repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository?owner=ralfes73&repository=hacs_ingstocks&category=integration)

1. Benutzerdefinierte Repositorie einbinden und herunterladen.
2. Starte Home Assistant neu.

## Konfiguration

Suche nach dem ISIN Code auf https://www.ing.de/

Füge in deiner `configuration.yaml` folgenden Abschnitt hinzu:

```yaml
sensor:
  - platform: ingstocks
    isin: "DE000BASF111"
    scan_interval: 300  # Optional - Alle 5 Minuten (300 Sekunden)
  - platform: ingstocks
    isin: "US5949181045"
```