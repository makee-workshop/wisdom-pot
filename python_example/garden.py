import time
import sys  
import websocket
import datetime
sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

websocket.enableTrace(True)
ws = websocket.create_connection("ws://wot.city/object/5618c14bc9fca6d51a000900/send")


while True:
	h0 = value.get("H0")
	t0 = value.get("T0")
	l0 = value.get("L0")
	d0 = value.get("D0")
	
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	
	vals = "{\"date\":\""+date+"\",\"h\":"+h0+",\"temperature\":"+t0+",\"l\":"+l0+",\"d\":"+d0+"}"
	
	time.sleep(1);
	ws.send(vals);
	print vals;
