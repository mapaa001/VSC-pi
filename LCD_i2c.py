import I2c_LCD_driver
from time import *

mylcd = I2c_LCD_driver.lcd()

mylcd.lcd_display_string("Heisann lol! :D", 2)