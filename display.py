import ssd1306
from machine import Pin, SoftI2C

class Display:
    def __init__(self):
        # ESP32 Pin assignment
        self.i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        self.oled_width = 128
        self.oled_height = 64
        self.oled = ssd1306.SSD1306_I2C(self.oled_width, self.oled_height, self.i2c)
        self.oled.fill(0)
        
    def clear(self):
        self.oled.fill(0)

    def text(self, text:str, ypos:int) -> None:
 #       self.oled.fill(0)
        self.oled.text(text, 0, ypos, 0xffff)
    
    def show(self) -> None:
        self.oled.show()
