import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

echo = 23
trig = 24

GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT

)