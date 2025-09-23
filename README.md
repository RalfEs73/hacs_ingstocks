# ING Stocks Home Assistant Integration

Mit dieser benutzerdefinierten Integration kannst du Aktienkurse von ING direkt als Sensor in Home Assistant einbinden.

## Features

- Abruf von Aktienkursen über ING
- Anzeige von Preis, Währung, Kursänderung und weiteren Attributen
- Unterstützung für mehrere Aktien (ISINs)
- Automatische Aktualisierung (z. B. alle 5 Minuten)

## Installation

Die empfohlene Methode ist die Installation über HACS.
1. Repro einbinden
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