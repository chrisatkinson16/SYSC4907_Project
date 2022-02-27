# SYSC 4907 IOT project
# @description Returns collected values
# @author Chris Atkinson, Kevin Belanger
# @version Version 1, October 15th 2021

import requests
import json
import urllib.parse
import http.client
import time
import RPi.GPIO as GPIO
import time
import random

key = "LQ1LYNA564IB0EX5"  # Server RPi write key
channel = 21  # To be used later to access Pin 40: GPIO21 on the RPi
GPIO.setmode(GPIO.BCM)  # Setting up GPIO input/output pin naming scheme to BCM (Broadcom SOC Channel)
# to access GPIO21 by simply using "channel" which was set in the previous line
GPIO.setup(channel, GPIO.IN)  # Sets GPIO21 to an input pin


# function that establishes connection between Data collector RPi and Server RPi using Thingspeak Data collector RPi
# channel key and json
def readServerRPi():
    URL = 'https://api.thingspeak.com/channels/1155565/feeds.json?api_key=8JDWE6GONX7QWNAR&results=2'  # URL for thingspeak channel
    KEY = '8JDWE6GONX7QWNAR'  # Data collector RPi read key
    HEADER = '&results=2'
    NEW_URL = URL + KEY + HEADER
    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_1 = get_data['feeds']
    return field_1[0]


# function that prints a statement depending on wether or not there are poeple in the office
def isOccupied(channel):
    if GPIO.input(channel):
        print("no people in office")
        i = 0
    else:
        print("people in the office")
        i = 1
    return i


GPIO.add_event_detect(channel, GPIO.BOTH,
                      bouncetime=300)  # detects both rising and falling edge and sets debounce time to 300 ms
# this allows for readings from moisture sensor to be taken everytime they change state between Boolean 1 and 0
GPIO.add_event_callback(channel,
                        isOccupied)  # Calls getMoisture back to run again to stay up to date on chnaging state between Boolean 1 and 0


# function that simulates Temperature sensor, producing random values between 15 and 25
def getTemp():
    return random.randint(150, 250) / 10


# function that sends temperature and Occupancy values collected to the Server RPi using the json code above and
# linking with server pi key "occupancy" is either a 1 or a 0, and "Temperature" is a randint between 15 and 25
# prints moisture and Temperature once they are delivered to Server RPi
def transmission():
    while True:
        occupancy = isOccupied(channel)
        temperature = getTemp()
        params = urllib.parse.urlencode({'field1': occupancy, 'field2': temperature, 'key': key})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(occupancy)
            print(temperature)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break


# endless while loop, checks to see if the ID sent from Server RPi in "field1' is meant for this Data collector RPi
# in this case, the ID for this RPi is set to 4, so if Server RPi wants to access this Data Collector RPi,
# the Server RPi must send "4" in "field1"
while True:
    currentID = readServerRPi()['entry_id']
    field = readServerRPi()
    if field['entry_id'] > (currentID):
        currentID = field['entry_id']
        if field['field1'] == '5':  # Checks if the server RPi is sending a request to this RPi
            transmission()
            print(field['field2'])
