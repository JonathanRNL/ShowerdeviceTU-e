from math import log


# constants
Beta = 3977 # characteristic thermistor value
Kelvin_constant = 273.15
R1 = 50000
R298 = 35000 # resistance of termistor at 298.15K
Vavdd = 3.3 # reference voltage and source voltage to the divider (3.3 V)

# functions
def adc_to_celsius(v):
    return ((1 / (log(1/(R1*v/(R298*(Vavdd-v))))/Beta + 1/298.15)) - Kelvin_constant)
