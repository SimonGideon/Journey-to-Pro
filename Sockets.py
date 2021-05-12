#  Sending dat via UDP
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
msg = ("Hello you there!").encode('utf-8') # socket.sendto() takes bytes as input, hence we must
# encode the string first.
s.sendto(msg, ('localhost', 6667))



# Web sockets.
# Simple Echo with aiohttp
import asyncio
from aiohttp import ClientSession
with ClientSession() as session:
    async def hello_world():
        websocket = await session.ws_connect("wss://echo.websocket.org")
        websocket.send_str("Hello, world!")
        print("Received:", (await websocket.receive()).data)
        await websocket.close()


    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())


# Wrapper Class with aiohttp.
import asyncio
from aiohttp import ClientSession
class EchoWebSocket(ClientSession):
    URL = "wss://echo.websocket.org"

    def __init__(self):
        super().__init__()
        self.websocket = None

    async def connect(self):
        """Connect to the WebSockt."""
        self.websocket = await self.ws_connect(self.URL)
    async def send(self, message):
        """Send a message to the WebSocket."""
        assert self.websocket is not None, "You must connect first!"
        self.websocket.send_str(message)
        print("Sent:", message)

    async def receive(self):
        """Receive one message from the WebSocket."""
        assert self.websocket is not None, "You must connect first!"
        return (await self.websocket.receive()).data

    async def receive(self):
        """Receive one message from the WebSocket."""
        assert self.websocket is not None, "You must connect first!"
        return (await self.websocket.receive()).data

    async def read(self):
        """Read messages from the WebSocket."""
        assert self.websocket is not None, "You must connect first!"
        while self.websocket.receive():
            message = await self.receive()
            print("Received:", message)
            if message == "Echo 9!":
                break
async def send(websocket):
    for n in range(10):
        await websocket.send("Echo {}!".format(n))
        await asyncio.sleep(1)
loop = asyncio.get_event_loop()
with EchoWebSocket() as websocket:
    loop.run_until_complete(websocket.connect())
    tasks = (
        send(websocket),
        websocket.read()
    )
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()






