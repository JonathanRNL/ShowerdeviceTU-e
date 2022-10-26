import time
from wlan import Wlan
from display import Display
from flow import FlowMeter
from temperature import TemperatureMeter
from cloud import Cloud
from timer import convert
from temp_conversion import adc_to_celsius
import storage

# --- Begin configuration --- 
ssid = 'lilygo'
password = 'lilygo123'
url = 'https://nwigsvkiq4reugluegyn5ovdxa0qagdp.lambda-url.eu-central-1.on.aws/'
# --- End configuration ---


display = Display()

wlan = Wlan()
wlan.printNetworks()
wlan.connect(ssid, password)

flow_meter = FlowMeter()
flow_meter.start()

temperature_meter = TemperatureMeter()

cloud = Cloud(url)


time_stamp_at_start = time.time()
n_counter = 0
n_counter_2 = 0
temp_sum = 0
duration = 0
# Infinite main program loop
while True:
    try:
        n_counter += 1
        temp = adc_to_celsius(temperature_meter.readTemp())
        temp_rounded = int(round(temp))
        temp_sum += temp
        temp_average = temp_sum/n_counter
        storage.write_file("temperature.txt", temp_average) 
        volume = int(flow_meter.readFlow())
        volume_2 = flow_meter.readFlow_2()
        storage.write_file("volume.txt", volume) 
        time_stamp = time.time()
        if volume_2 > 0.005: #flow treshold
            n_counter_2 += 3.5 #change if needed due to lag
            duration:str = convert(n_counter_2)
            storage.write_file("timer.txt", duration) 
        duration_read_storage = storage.read_file("timer.txt")
        display.clear()
        display.text(f'Water: {volume} liters', 10)
        display.text(f'Degrees: {temp_rounded}', 25)
        display.text(f'Time: {duration_read_storage}', 50)
        display.show()
        #print(f'average temp {temp_average}')
        #print(f'time:{duration}')
        #print(f'volume: {volume_2}')      
        cloud.sendData({ 'timestamp': time_stamp, 'temp': temp_average, 'volume': volume})        
    except Exception as ex:
        print('Exception', str(ex))
        pass
    time.sleep(1)
