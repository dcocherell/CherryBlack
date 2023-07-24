# consumers.py

from channels.consumer import AsyncConsumer
from .tasks import update_stocks
import threading

class StocksConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
    
    async def websocket_receive(self, event):
        print("receive", event)
        thread = threading.Thread(target=update_stocks)
        thread.start()

    async def websocket_disconnect(self, event):
        print("disconnected", event)
