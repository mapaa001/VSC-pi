import RPi  .GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #alternative GPIO.BOARD

signal = 21

GPIO.setup(signal, GPIO.IN)

try:
    while 1:    #TRUE = 1
        val = GPIO.input(signal) #read FC-51 out pin 
        while val == 1:
            print("motion detected! xD")
        time.sleep(0.5)
except KeyboardInterrupt: #stop program with CTRL + C
    print ("setting all GPIO pins to default") 
    GPIO.cleanup()  #set all GPIO to default state
    print("exiting program")