# IoT Light Scheduler Dashboard

A real-world simulation of IoT-based light scheduling using WebSockets, MQTT, and Arduino.

## Features
- Web interface to set ON/OFF times.
- MQTT message broker for communication.
- Serial control of Arduino to toggle lights.

## Tech Stack
- Frontend: HTML, CSS, JS
- Backend: Python (websockets, subprocess)
- Messaging: Mosquitto (MQTT)
- Hardware: Arduino UNO + Relay

## How to Run

1. Start Mosquitto broker:
   ```bash
   mosquitto
