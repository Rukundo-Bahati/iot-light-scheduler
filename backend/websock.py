import asyncio
import websockets
import json
import subprocess

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        schedule = f"{data['1']},{data['0']}"
        print("Publishing to MQTT:", schedule)
        subprocess.run(["mosquitto_pub", "-t", "iot/light/schedule", "-m", schedule])

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
