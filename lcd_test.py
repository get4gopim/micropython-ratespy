"""
Tutorials
- Raspberry Pi Pico - LCD I2C 16x2: https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-lcd-i2c
- Raspberry Pi Pico - LCD I2C 20x4: https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-lcd-20x4
- ESP32 MicroPython - LCD I2C 16x2: https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-lcd-i2c
- ESP32 MicroPython - LCD I2C 20x4: https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-lcd-20x4
"""

from machine import I2C, Pin
from lcddriver import LCD_I2C
import utime

# The I2C address of your LCD (Update if different)
I2C_ADDR = 0x27  # Use the address found using the I2C scanner

# Define the number of rows and columns on your LCD
LCD_ROWS = 2
LCD_COLS = 16

# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# Initialize LCD
lcd = LCD_I2C(i2c, I2C_ADDR, LCD_ROWS, LCD_COLS)

# Setup function
lcd.backlight_on()
lcd.clear()

lcd.clear()
lcd.set_cursor(3, 0) 
lcd.print("ABCD")
utime.sleep(2)
