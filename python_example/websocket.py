from __future__ import print_function
import websocket
import sys
import time
from threading import Thread

def send(url, value):
    websocket.enableTrace(False)
    ws = websocket.create_connection(url)
    ws.send(value)
    ws.close()

class Service(Thread):
	enable = False
	def __init__(self):
		super(Service, self).__init__()
	def startService(self):
		self.enable = True
		self.start()
		print("start service")
	def stopService(self):
		self.enable = False
		print("stop service")
	def run(self):
		print(self.enable)
		while self.enable==True:
			send("ws://wot.city/object/5618c14bc9fca6d51a000900/send", "{\"temperature\":2}")
			"""print("sned")"""
			"""print(self.enable)"""
			time.sleep(1)
		print("stop run")

service = Service()
"""service.startService()"""

print("select service")
print("1: start service")
print("2: stop service")
print("9: exit")

cmd = True;
while cmd:
    try:
	print("waiting command")
        x = int(raw_input())
	if x==9:
		cmd = False
		break
	elif x==1:
		service.startService()
	elif x==2:
		service.stopService()
	else:
		print("unknown command")
    except ValueError:
        print("Wrong Number")
print("Exit")
service.join()
