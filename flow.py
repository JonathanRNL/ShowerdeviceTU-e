from machine import Pin, Timer
import time

class FlowMeter:
    def __init__(self):
        self.counter_pin = Pin(35, Pin.IN)
        self.switch = Pin(02, Pin.IN)
        self.volume = 0
        self.counter = 0
        self.tim = Timer(1)
        def mycallback(t):
            self.counter = 0
            pass
        self.tim.init(mode=Timer.PERIODIC, period=1000, callback=mycallback)

    def interrupt_handler(self, pin):  
        self.counter += 1
        
    def start(self):
        self.counter_pin.irq(trigger=Pin.IRQ_RISING, handler=self.interrupt_handler)
        self.switch.irq(trigger=Pin.IRQ_FALLING, handler=self.reset)
    def reset(self, pin):
        self.counter = 0
        self.volume = 0
        
    def readFlow(self) -> int:
        previousvolume= self.volume
        self.volume = (self.counter/11)/60 + previousvolume
        return self.volume
    
    def readFlow_2(self) -> int:
        self.volume_2 = ((self.counter/11))/60
        return self.volume_2
