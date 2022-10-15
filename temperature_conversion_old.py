#!/usr/bin/env python
# coding: utf-8

# In[8]:


from time import sleep
from machine import ADC
from math import log
#import time, sys

## constants
Beta = 3977 # characteristic thermistor value
Kelvin_constant = 273.15
R1 = 10000
R298 = 100000 # resistance of termistor at 298.15K
Vavdd = 3.3 # reference voltage and source voltage to the divider (3.3 V)

## functions
def adc_to_celsius(v):
    return(1 / (log(1/(R1*v/(R298*(Vavdd-v))))/Beta + 1/298.15)) - Kelvin_constant

## setup
thermistor_pin = ADC(26) # should we use ADC pin or just the same pin as flow sensor? since it is flow & temp sensor in 1

## Loop
while True:
    thermistor_value = thermistor_pin.read_u16()
    print(thermistor_value, round(adc_to_celsius(thermistor_value), 1)
    sleep(0.1)


# In[ ]:




