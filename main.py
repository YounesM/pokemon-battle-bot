import asyncio
import websockets
import requests

async def main():
    """
    Trying stuff
    """
    async with websockets.connect('ws://sim.smogon.com:8000/showdown/websocket') as websocket:
        while True:
            message = await websocket.recv()
            print(message)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
