import serial
import schedule
import time
from datetime import datetime
import paho.mqtt.client as mqtt

# Configuration
SERIAL_PORT = 'COM5'  # Change to your Arduino's port
BAUD_RATE = 9600
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 8000
TOPIC_SCHEDULE_ON = "light/schedule/on"
TOPIC_SCHEDULE_OFF = "light/schedule/off"

# Serial connection
# try:
#     arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
#     time.sleep(2)  # Wait for connection
#     print("✅ Connected to Arduino")
# except Exception as e:
#     print(f"❌ Error connecting to Arduino: {e}")
#     exit()

def turn_on_light():
    arduino.write(b'1\n')
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Light ON")

def turn_off_light():
    arduino.write(b'0\n')
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Light OFF")

def set_schedule(on_time, off_time):
    schedule.clear()
    schedule.every().day.at(on_time).do(turn_on_light)
    schedule.every().day.at(off_time).do(turn_off_light)
    print(f"📅 Schedule set: ON at {on_time}, OFF at {off_time}")

def on_connect(client, userdata, flags, rc):
    print(f"🔌 Connected to MQTT broker (code {rc})")
    client.subscribe(TOPIC_SCHEDULE_ON)
    client.subscribe(TOPIC_SCHEDULE_OFF)

def on_message(client, userdata, msg):
    global on_time, off_time
    payload = msg.payload.decode().strip()
    print(f"[MQTT] {msg.topic}: {payload}")

    if msg.topic == TOPIC_SCHEDULE_ON:
        try:
            time.strptime(payload, "%H:%M")
            on_time = payload
            if off_time:
                set_schedule(on_time, off_time)
        except ValueError:
            print("❗ Invalid ON time format")
    elif msg.topic == TOPIC_SCHEDULE_OFF:
        try:
            time.strptime(payload, "%H:%M")
            off_time = payload
            if on_time:
                set_schedule(on_time, off_time)
        except ValueError:
            print("❗ Invalid OFF time format")

on_time = ""
off_time = ""

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_start()
        
        print("📡 Listening for MQTT schedules...")
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Stopped by user")
    finally:
        client.loop_stop()
        arduino.close()