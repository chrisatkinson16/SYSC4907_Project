import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 23
GPIO.setup(PIR_PIN, GPIO.IN)

print("Starting up PIR sensor")
time.sleep(2)
print("Ready")

while True:
    if GPIO.input(PIR_PIN):
        print("Motion Detected")
    else:
        print("No Motion")
    time.sleep(6)
        
