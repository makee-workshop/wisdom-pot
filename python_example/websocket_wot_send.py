import websocket
import sys
import time
websocket.enableTrace(True)
ws = websocket.create_connection("ws://wot.city/object/5618c14bc9fca6d51a000900/send")
while True:
	ws.send( "{\"temperature\":2}")
        """print("sned")"""
        """print(self.enable)"""
        time.sleep(1)
