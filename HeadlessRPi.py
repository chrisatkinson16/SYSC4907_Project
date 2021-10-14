# L1-F-4 Water plEase
# @description Returns collected moisture and pH values from Data collector RPi to Server RPi
# @author Conor Johnson Martin & Chris Atkinson
# @version Version 1, 24 November 2020

import requests
import json
import urllib.parse
import http.client
import time
import RPi.GPIO as GPIO
import time
import random

key = "LQ1LYNA564IB0EX5"     # Server RPi write key
channel = 21		     # To be used later in function getMoisture to access Pin 40: GPIO21 on the RPi
GPIO.setmode(GPIO.BCM)       # Setting up GPIO input/output pin naming scheme to BCM (Broadcom SOC Channel) to access GPIO21 by simply using "channel" which was set in the previous line
GPIO.setup(channel, GPIO.IN) # Sets GPIO21 to an input pin

# function that establishes connection between Data collector RPi and Server RPi using Thingspeak Data collector RPi channel key and json
def readServerRPi():
    URL = 'https://api.thingspeak.com/channels/1155565/feeds.json?api_key=8JDWE6GONX7QWNAR&results=2' # URL for thingspeak channel
    KEY = '8JDWE6GONX7QWNAR'  # Data collector RPi read key
    HEADER = '&results=2'                     
    NEW_URL = URL + KEY + HEADER             
    get_data = requests.get(NEW_URL).json()   
    channel_id = get_data['channel']['id']
    field_1 = get_data['feeds']
    return (field_1)[0]

# function that prints a statement depending on what the moisture sensor is observing
# Returns Boolean "i"
# i is 0 if no water, else i is 1
# Value stored in i is what is sent to Server RPi, which uses this data in GUI and Database
def getMoisture(channel):
    if GPIO.input(channel):
        print("no water detected")
        i = 0
    else:
        print("water detected")
        i = 1
    return i

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # detects both rising and falling edge and sets debounce time to 300 ms
                                                           # this allows for readings from moisture sensor to be taken everytime they change state between Boolean 1 and 0
GPIO.add_event_callback(channel, getMoisture)              # Calls getMoisture back to run again to stay up to date on chnaging state between Boolean 1 and 0

# function that simulates pH sensor, producing random values between 6.0 and 8.0
def getpH():
    return random.randint(35,90)/10

# function that sends the moisture and pH values collected to the Server RPi using the json code above and linking with server pi key
# "moisture" is either a 1 or a 0, and "pH" is a randint between 0.35 and 0.9
# prints moisture and pH once they are delivered to Server RPi
def transmission():
    while True:
        moisture = getMoisture(channel)
        pH = getpH()
        params = urllib.parse.urlencode({'field1': moisture,'field2': pH, 'key': key})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(moisture)
            print(pH)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break


# endless while loop, checks to see if the ID sent from Server RPi in "field1' is meant for this Data collector RPi
# in this case, the ID for this RPi is set to 4, so if Server RPi wants to access this Data Collector RPi, the Server RPi must send "4" in "field1"

while True:
    currentID = readServerRPi()['entry_id']
    field = readServerRPi()
    if field['entry_id'] > (currentID):
        currentID = field['entry_id']
        if field['field1'] == '5':  # Checks if the server RPi is sending a request to this RPi
            transmission()
            print(field['field2'])
