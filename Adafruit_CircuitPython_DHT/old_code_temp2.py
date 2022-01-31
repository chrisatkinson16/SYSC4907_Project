import board
import adafruit_dht
import time
dht = adafruit_dht.DHT11(board.D23)

while(1):
    print(dht.temperature)
    print(dht.humidity)
    time.sleep(3)