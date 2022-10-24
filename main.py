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
# Infinite main program loop
while True:
    try:        
        temp = temperature_meter.readTemp()
        volume = flow_meter.readFlow()
        time_stamp = time.time()
        duration:str = convert(time_stamp - time_stamp_at_start)
        display.clear()
        display.text(f'Temperature:{temp}°', 10)
        display.text(f'Water:{volume} liters', 30)
        display.text(f'Time:{duration}', 50)
        display.show()
        print(f'time:{duration}')
        cloud.sendData({ 'timestamp': time_stamp, 'temp': temp, 'volume': volume})        
    except Exception as ex:
        print('Exception', str(ex))
        pass
    time.sleep(1)
