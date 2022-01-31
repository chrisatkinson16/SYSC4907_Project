# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# for now run "ps aux | grep libgpiod_pulsein" to find the pid of the running process
# then run "sudo kill PID" to kill it to let the system rerun the code on the same GPIO

import paho.mqtt.client as mqtt
import time
import board
import adafruit_dht
from datetime import date
from datetime import datetime

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D18)



def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)


# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)
file = open("test.txt", "w")
file.write("Temperature\tDate\tTime\n")
while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    
    temp_hum_str = 'The temperature is ' + str(temperature_c) + ' degrees right now'
    client.publish('raspberry/topic', payload=temp_hum_str, qos=0, retain=False)
    print(f"send: {temp_hum_str} C to raspberry/topic")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    now = datetime.now().time()
    file.write(str(temperature_c) + "\t" + d1 + "\t" + str(now) + "\n")
    file.flush()
    time.sleep(2.0)
client.loop_forever()

