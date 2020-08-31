import socket
import serial
import pynmea2
import time
def parseGPS(str, s):
	if str.find('GGA')>0:
		print str
		msg = pynmea2.parse(str)
		print "Lat: %s %s -- Lon: %s %s" %(msg.lat, msg.lat_dir, msg.lon, msg.lon_dir)
		msg = msg.lat +msg.lat_dir + ", " + msg.lon + msg.lon_dir
		print "msg : " + msg
		s.send(msg.encode(encoding='utf_8',errors = 'strict'))
		print "receving data........."
		data = s.recv(1024)
		print 'result: ' + (data.decode())
		
HOST = '192.168.123.102'
PORT = 34190

serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
	#s.connect((HOST, PORT))
	str = serialPort.readline()
	parseGPS(str, s)

s.close()
