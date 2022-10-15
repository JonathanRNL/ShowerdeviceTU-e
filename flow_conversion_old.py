#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python

import RPi.GPIO as GPIO # import RPi.GPIO module
import time, sys

FLOW_SENSOR = 13 # number of pin ???

GPIO.setmode(GPIO.BCM) # choose BCM or board
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # input selected and definition of which function should be called (from HIGH to LOW)

global count
count = 0

def countPulse(channel): # function that is called when the voltage applied to the GPIO changes
    if start_counter == 1:
        count = count+1
        print(count)

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse)

while True: # infinite loop
    try:
        start_counter = 1 # activate the counter
        time.sleep(1) # wait for 1 second
        start_counter = 0 # start_counter is reset
        flow = (count / 11) # Pulse frequency (Hz) = 11Q, Q is flow rate in L/min.
        print("The flow is: %.3f Liter/min" % (flow)) # flow rate is printed for the previous second
        count = 0 # reset the pulse counter so we can calculate the flow per minute
        time.sleep(5) # WHY wait 5 secs ?????
    except KeyboardInterrupt: # stop the counter completely if it is manually interrupted, resets all pins used by this program
        print('\nkeyboard interrupt!')
        GPIO.cleanup()
        sys.exit()


# In[ ]:




