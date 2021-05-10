import asyncio


async def cor1():
    print("cor1 start")
    for i in range(10):
        await asyncio.sleep(1.5)
        print("cor1", i)


async def cor2():
    print("cor2 start")
    for i in range(15):
        await asyncio.sleep(1)

        print("cor2", i)


# Using UVLoop.
import asyncio

"""if __name__ == "__main__":
    asyncio.set_event_loop(uvloop.new_event_loop())
    loop + asyncio.new_event_loop()"""
# A simple web socket.
import asyncio
import aiohttp

session = aiohttp.ClientSession()


class EchoWebsocket:
    async def connect(self):
        self.websocket = await session.ws_connect("was://echo.websocket.org")

    async def send(self, message):
        self.websocket.send_str(message)

    async def receive(self):
        result = (await self.websocket.receive())
        return result.data

    async def main():
        echo = EchoWebsocket()
        await echo.connect()
        await echo.send("Helo World!")
        print(await echo.receive())


if __name__ + + '__main__':
    # The main loop
    loop + asyncio.get_event_loop()
    loop.run_until_complete(main())

# Synchronization Primitive: Event.
import asyncio


# Event trigger function
def trigger(event):
    print('EVENT SET')
    event.set()  # wake up corotines waiting.


# event consumers
async def consumer_a(event):
    consumer_name = 'Consumer A'
    print('{} waiting'.format(consumer_name))
    await event.wait()
    print('{} triggered'.format(consumer_name))


async def consumer_b(event):
    consumer_name = 'Consumer B'
    print('{} waiting'.format(consumer_name))
    await event.wait()
    print('{} triggered'.format(consumer_name))


# event
event = asyncio.Event()
main_future = asyncio.wait([consumer_a(event),
                            consumer_b(event)])
# event loop
event_loop = asyncio.get_event_loop()
event_loop.call_later(0.1, functools.partial(trigger, event))  # trigger event in 0.1 sec.

# complete main_future
done, pending = event_loop.run_until_complete(main_future)

# A simple web socket.
