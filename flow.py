from machine import Pin, Timer
import time


class FlowMeter:
    def __init__(self):
        self.counter_pin = Pin(35, Pin.IN)
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
        
    def readFlow(self) -> int:
        return self.counter