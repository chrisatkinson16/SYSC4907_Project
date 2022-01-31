#!/usr/bin/env python3

# 2020-09-27
"""
    A Program to read the DHTXX temperature/humidity sensors.

    REQUIREMENTS
    DHT.py    download "module" from http://abyz.me.uk/rpi/pigpio/code/DHT.py
    pigpiod running
"""

import sys
import pigpio
import DHT
import time
import datetime

# Sensor should be set to DHT.DHT11, DHT.DHTXX or DHT.DHTAUTO
sensor = DHT.DHT11

pin = 4     # Data - Pin 7 (BCM 4)

def output_data(timestamp, temperature, humidity):
    # Sample output Date: 2019-11-17T10:55:08, Temperature: 25°C, Humidity: 72%
    date = datetime.datetime.fromtimestamp(timestamp).replace(microsecond=0).isoformat()
    print(u"Date: {:s}, Temperature: {:g}\u00b0C, Humidity: {:g}%".format(date, temperature, humidity))

pi = pigpio.pi()
if not pi.connected:
  exit()

s = DHT.sensor(pi, pin, model = sensor)

tries = 5   # try 5 times if error
while tries:
    try:
        timestamp, gpio, status, temperature, humidity = s.read()   #read DHT device
        if(status == DHT.DHT_TIMEOUT):  # no response from sensor
            exit()
        if(status == DHT.DHT_GOOD):
            output_data(timestamp, temperature, humidity)
            exit()      # Exit after successful read
        time.sleep(2)
        tries -=1
    except KeyboardInterrupt:
        break