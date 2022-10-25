import time
from wlan import Wlan
from display import Display
from flow import FlowMeter
from temperature import TemperatureMeter
from cloud import Cloud
from timer import convert
from temp_conversion import adc_to_celsius

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
temp_sum = 0
# Infinite main program loop
while True:
    try:
        n_counter += 1
        temp = adc_to_celsius(temperature_meter.readTemp())
        temp_rounded = round(temp)
        temp_sum += temp
        temp_average = temp_sum/n_counter
        volume = int(flow_meter.readFlow())
        time_stamp = time.time()
        duration:str = convert(time_stamp - time_stamp_at_start)
        display.clear()
        display.text(f'Water:{volume} liters', 10)
        display.text(f'Degrees:{temp_rounded}', 25)
        display.text(f'Time:{duration}', 50)
        display.show()
        cloud.sendData({ 'timestamp': time_stamp, 'temp': temp_average, 'volume': volume})        
    except Exception as ex:
        print('Exception', str(ex))
        pass
    time.sleep(1)
