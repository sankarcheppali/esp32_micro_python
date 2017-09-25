import machine
import socket
import time
import network
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect('DangerVirus', 'abivarsh@2016')
  while not sta_if.isconnected():
    pass
print('network config:', sta_if.ifconfig())
html='''<!DOCTYPE html>
<html>
<head><title>ESP32 LED on/off</title></head>
<center><h2>WebServer for turning LED on </h2></center>
<form>
<button name="LED" value='ON' type='submit'> LED ON </button>
<button name="LED" value='OFF' type='submit'> LED OFF </button>
<br><br>
'''
LED0 = machine.Pin(16,machine.Pin.OUT)
LED0.value(0)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)
while True:
  conn,addr=s.accept()
  print("GOT a connection from %s" % str(addr))
  request=conn.recv(1024)
  print("Content %s" % str(request))
  request=str(request)
  LEDON=request.find('/?LED=ON')
  LEDOFF=request.find('/?LED=OFF')
  if(LEDON==6):
    LED0.value(1)
  if(LEDOFF==6):
    LED0.value(0)
  response=html
  conn.send(response)
  conn.close()
  
  
