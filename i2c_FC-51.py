from tokenize import blank_re
import RPi.GPIO as GPIO
import time
import LCD_i2c
import I2c_LCD_driver

sensor = 21

mylcd = I2c_LCD_driver.lcd()

GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor,GPIO.IN)

mylcd.lcd_display_string ("IR Sensor Klar.....", 1)

try:
    while True:    #True = 1
        if GPIO.input(sensor)==0:
            mylcd.lcd_display_string("Heisann lol! :D", 2)
            time.sleep(0.5)
        else:
            mylcd.lcd_display_string("Ingen hindring!!", 2)
            time.sleep(0.5)
except KeyboardInterrupt:
    mylcd.lcd_display_string ("setting all GPIO pins to default", 1) 
    GPIO.cleanup()  #set all GPIO to default state
    mylcd.lcd_display_string ("exiting program", 2)
    time.sleep(1)
    mylcd.lcd_display_string ("                 ",1)
    mylcd.lcd_display_string ("                 ",2)