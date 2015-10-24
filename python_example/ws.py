"""from websocket import create_connection"""
import websocket
ws = websocket.WebSocket()
ws.connect("wss://echo.websocket.org")
"""ws = websocket.create_connection("ws://echo.websocket.org/")"""
print "Sending 'Hello, World'..."
ws.send("Hello, World")
print "Sent"
print "Receiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()
