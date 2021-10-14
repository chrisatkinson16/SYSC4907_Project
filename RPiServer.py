# L1-F-4 Water plEase
# Server RPi code
# @author Chris Atkinson, Kevin Belanger
# @version Version 1, 24 November 2020

import requests
import json
import urllib.parse
import http.client
import time
import sqlite3

# set up a cursor for the database
dbconnect = sqlite3.connect("/Users/User/Downloads/SQLiteStudio/plant_database.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
# select the whole database
cursor.execute('SELECT * FROM plant_database')

# Set up arrays for the values in the database
id = []
plantName = []
expectedMoisture = []
pHmin = []
pHmax = []

# Populate the values in the arrays with values from the database
for row in cursor:
    id.append(row['ID'])
    plantName.append(row['Plant Name'])
    expectedMoisture.append(row['Moisture'])
    pHmin.append(row['pH min'])
    pHmax.append(row['pH max'])

#  This function checks that the connection to the server is good. and sends a confirmation message back to the headless RPi
def transmission(field1 = None, field2= None, field3= None, field4= None, field5= None, field6= None, field7= None, field8= None):
    key = "H8QD218BNTIQL7OQ"  # Headless RPi write key
    params = urllib.parse.urlencode({'field1': field1, 'field2': field2, 'field3': field3, 'field4': field4, 'field5': field5, 'field6': field6, 'field7': field7, 'field8': field8, 'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        conn.close()
    except:
        print("connection failed")

# This function requests the data from the headless RPi and returns it.
def readHeadlessPi():
    url = 'https://api.thingspeak.com/channels/1160322/feeds.json?api_key=HTDCLD7F8EWCLS4L&results=2' # Server RPi read URL
    key = 'HTDCLD7F8EWCLS4L'  # Server RPi read key
    header = '&results=1'

    finalURL = url + key + header

    get_data = requests.get(finalURL).json()

    channel1read = get_data['feeds'][0]

    return channel1read

currentID = readHeadlessPi()['entry_id']

transmission(4, 'test')

broken = 0 # This variable stops the while loop from being infinite.
# This while loop runs until either the timer times out or it gets a reading from the headless RPi.
while(True):
    broken +=1
    if broken == 2:  # if there is no connection for 200 seconds then the loop ends.
        break
    if readHeadlessPi()['entry_id'] == (currentID+1):  # if the RPi establishes a connection and reads values then the loop stops.
        break
    time.sleep(0.1)

print(readHeadlessPi()['field1'])  # These two prints confirm that the RPi has read the correct information.
print(readHeadlessPi()['field2'])
moisture = int(readHeadlessPi()['field1'])  # Set moisture and pH variables to be used in later functions.
pH = float (readHeadlessPi()['field2'])

# This function compares the moisture that was found by the sensor and compares it ot the expected moisture which is 1
# and returns 1 or 0 accordingly.
def compareMoisture(j):
    if (moisture == expectedMoisture[j]):
        return 1  # If the soil is moist return 1.
    else:
        return 0  # If not return 0.

# This function compares the pH to the expected pH value that depends on the plant.
# Returns 1 if pH is good and 0 if not.
def comparepH(k):
    if(pHmin[k] < pH) & (pH < pHmax[k]):
        return 1  # If pH is within expected range return 1.
    else:
        return 0  # If not return 0.

# This function checks the compareMoisture() function to see if the plant needs water
# and returns the message required.
def giveWater(l):
    x = ' '  # Create a local variable that stores the string for later use.
    if(compareMoisture(l) == 0):
        x = "Water plEase"  # If compareMoisture() is 0 that means it needs water so the function sets x accordingly.
    else:
        x = "No water needed"  # If compareMoisture() is 1 then no action is required.
    return x

# This function checks if the comparepH() function has flagged a need for pH supplements or not
# and returns the message required.
def givepHSuppliment(m):
    y = ' '
    if(comparepH(m) == 0):
        y = "Give pH suppliment"  # If comparepH() is 0 that means it needs a pH supplement so the function sets y accordingly.
    else:
        y = "pH is sufficient"  # If compareMoisture() is 1 then no action is required.
    return y

# Gets user data to set the plant that they have.
def setPlant():
    userPlant = plantName[0]

# prints the current moisture
def printMoisture():
    print(moisture)

# prints the current pH
def printpH():
    print(pH)
