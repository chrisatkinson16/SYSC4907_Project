import paho.mqtt.client as mqtt
import time

temp = 'test'
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("raspberry/topic")


def on_message(client, uerdata, msg):
    print(f"{msg.payload}")
    global temp
    temp = f"{msg.payload}"

def run():
    client = mqtt.Client()
    client.loop_start()
    client.on_connect = on_connect
    client.on_message = on_message
    client.will_set('raspberry/status', b'{"status": "Off"}')
    client.connect("broker.emqx.io", 1883, 60)
    time.sleep(5)
    client.loop_stop()
    return temp[1:]
