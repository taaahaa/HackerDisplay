#watertest1

import RPi.GPIO as GPIO
import time

SENDER = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENDER, GPIO.IN)

while True:
    stuff = GPIO.input(SENDER) 
    print("Input is ", stuff)
    time.sleep(2)