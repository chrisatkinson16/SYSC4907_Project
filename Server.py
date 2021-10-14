# SYSC 4907 IOT project
# Server RPi code
# @author Chris Atkinson, Kevin Belanger
# @version Version 1, October 15th 2021

import requests
import json
import urllib.parse
import http.client
import time
import sqlite3

# set up a cursor for the database
dbconnect = sqlite3.connect("/Users/User/Downloads/SQLiteStudio/userinfo_database.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
# select the whole database
cursor.execute('SELECT * FROM userinfo_database')

# Set up arrays for the values in the database
id = []
userName = []
expectedOccupancy = []
tempMin = []
tempMax = []

# Populate the values in the arrays with values from the database
for row in cursor:
    id.append(row['ID'])
    userName.append(row['Plant Name'])
    expectedOccupancy.append(row['Moisture'])
    tempMin.append(row['pH min'])
    tempMax.append(row['pH max'])

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
occupancy = int(readHeadlessPi()['field1'])  # Set moisture and pH variables to be used in later functions.
temp = float (readHeadlessPi()['field2'])

# This function compares the occupancy compares it to the expected occupancy which is 1
# and returns 1 or 0 accordingly.
def compareOccupancy(j):
    if (occupancy == expectedOccupancy[j]):
        return 1  # If occupied return 1.
    else:
        return 0  # If not return 0.

# This function compares the temperature to the expected temperature value that depends on the user preference.
# Returns 1 if temperature is good and 0 if not.
def compareTemp(k):
    if(tempMin[k] < temp) & (temp < tempMax[k]):
        return 1  # If temperature is within expected range return 1.
    else:
        return 0  # If not return 0.

# This function checks the compareOccupancy() function to see if the Office is occupied
# and returns the message required.
def checkOccupancy(l):
    x = ' '  # Create a local variable that stores the string for later use.
    if(compareOccupancy(l) == 0):
        x = "The office is occupied"  # If compareMoisture() is 0 that means it needs water so the function sets x accordingly.
    else:
        x = "The office is empty"  # If compareMoisture() is 1 then no action is required.
    return x

# This function checks if the compareTemp() function has flagged a need to raise the temperature or not
# and returns the message required.
def raiseTemp(m):
    y = ' '
    if(compareTemp(m) == 0):
        y = "fix the Temperature"  # If compareTemp() is 0 that means it needs to change the temperature so the function sets y accordingly.
    else:
        y = "Temperature is fine"  # If compareTemp() is 1 then no action is required.
    return y

# Gets user data to set the plant that they have.
def setName():
    user = userName[0]

# prints the current occupancy
def printOccupancy():
    print(occupancy)

# prints the current Temperature
def printTemp():
    print(temp)
