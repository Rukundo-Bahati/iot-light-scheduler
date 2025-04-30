IoT Light Scheduler Dashboard
Project Overview
This project simulates a real-world IoT dashboard to schedule a light using a graphical interface and network communication. The system allows users to set ON/OFF times for a light through a web interface, which then communicates via WebSocket to an MQTT broker. A Python subscriber receives the schedule and sends serial commands to an Arduino that controls the actual light relay.

System Architecture
<i>Browser Interface → WebSocket Server → MQTT Broker → Python Subscriber → Arduino → Light Relay</i>
Components
1. Frontend (Browser Interface)
HTML/CSS/JS dashboard

Input fields for ON and OFF times

Submit button to send schedule

2. WebSocket Server
Receives schedule from browser

Forwards schedule to MQTT using mosquitto_pub

3. MQTT Subscriber (Python)
Listens for schedule messages

Sends appropriate commands ('1' or '0') to Arduino via serial

4. Arduino UNO
Pre-programmed to act on serial input

Controls relay based on received commands

Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Python (websockets, pyserial)

Messaging: MQTT (mosquitto_pub/sub)

Hardware: Arduino UNO

Setup Instructions
Prerequisites
Python 3.x

Mosquitto MQTT broker

Arduino IDE (for Arduino programming)

Web browser with WebSocket support

Installation
Clone this repository

Install Python dependencies:

`pip install websockets pyserial paho-mqtt`
Set up Mosquitto MQTT broker

Upload Arduino sketch to your Arduino UNO

Usage
Start the WebSocket server

Start the MQTT subscriber script

Open the HTML dashboard in a browser

Set your desired ON/OFF times and submit

The system will automatically control the light based on your schedule
![alt text](<Screenshot From 2025-04-30 07-25-55.png>)

![alt text](<Screenshot From 2025-04-30 07-24-12.png>)
