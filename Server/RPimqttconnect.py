import paho.mqtt.client as mqtt #import the client1
import time

def on_message(client, userdata, message):
    if(str(message.payload.decode("utf-8")) != "hoj"):
        print("message received " ,str(message.payload.decode("utf-8")))




broker_address="broker.emqx.io"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
while(True):
    client.loop_start() #start the loop
    client.subscribe("raspberry/topic")
    time.sleep(4) # wait
    client.loop_stop() #stop the loop
    time.sleep(300)
