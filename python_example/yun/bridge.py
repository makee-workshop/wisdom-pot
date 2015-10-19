#!/usr/bin/python 
import sys     
sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient 
value = bridgeclient()

command="start"
while command!="stop":
	print(command)
