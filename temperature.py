from machine import ADC, Pin

class TemperatureMeter:
    def __init__(self):
        pin = Pin(34, Pin.IN)
        self.adc = ADC(pin)   			# create an ADC object acting on a pin
        self.adc.atten(ADC.ATTN_11DB)   # Full range: 3.3v
        
    def readTemp(self) -> int:
        return self.adc.read()  # read a raw analog value in the range 0-4096
   
