#!/usr/bin/env python
import time
import serial

def cleandata(b):
  s = str(b.decode('utf-8'))
  s = s.replace("\r", "")
  s = s.replace("\n", "")
  return s

ser = serial.Serial(
  port='/dev/ttyACM0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

counter=0

while 1:
  x = cleandata(ser.readline())
  if x == '' or x is None:
    continue
  print(x)
