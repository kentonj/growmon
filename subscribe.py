"""Subscribe to a websocket."""
import websockets
import asyncio

async def hello():
    async with websockets.connect("ws://localhost:8080/sensors/first/feed?clientId=kenton") as websocket:
        while True:
            res = await websocket.recv()
            print(res)

asyncio.run(hello())
