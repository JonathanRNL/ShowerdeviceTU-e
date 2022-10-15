#!/usr/bin/env python
# coding: utf-8

# In[5]:


import time

# constants
density_water = 0.997 # kg/L
specific_heat_water = 4182 #J/kg degC
energy_density_gas = 31700000 #J/m^3
water_price = 0.00089 # €/L
gas_price = 3.94 # €/m3


# measured quantities
T_shower = thermistor_value                       # temp measured by our sensor
T_cold = 15                                       # temp of the water entering the boiler (KNMI value)
T_hot = 80                                        # temp of the water when heated by the boiler (set by the user)
water_used = flow / 60                            # (L/min) amount of water measured by our flowsensor (IF WE MEASURE EVERY SECOND)


# calculations
ratio_hot_cold_water = (T_cold - T_shower) / (T_shower - T_hot)
mass_hot_water = (water_flow * density_water * ratio_hot_cold_water) / (1 + ratio_hot_cold_water) # kg

heat = mass_hot_water * specific_heat_water * (T_hot - T_cold) # J
gas_used = heat / energy_density_gas #(m3)

water_cost = water_used * water_price
gas_cost = gas_used * gas_price

total_cost = water_cost + gas_cost

print("The total cost is: %.3f euros" % (total_cost))


# In[ ]:




