import time
from wlan import Wlan
from display import Display
from flow import FlowMeter
from temperature import TemperatureMeter
from cloud import Cloud

# --- Begin configuration --- 
ssid = 'lilygo'
password = 'lilygo123'
url = 'https://nwigsvkiq4reugluegyn5ovdxa0qagdp.lambda-url.eu-central-1.on.aws/'
# --- End configuration ---


display = Display()
display.text('Shower monitor', 10)
display.text('Version 1.0.4', 20)
display.text('01/10/2022', 30)
display.show()

wlan = Wlan()
wlan.printNetworks()
wlan.connect(ssid, password)

flow_meter = FlowMeter()
flow_meter.start()

temperature_meter = TemperatureMeter()

cloud = Cloud(url)


# Infinite main program loop
while True:
    try:
        time_stamp = time.time()
        temp = temperature_meter.readTemp()
        flow = flow_meter.readFlow()
        cloud.sendData({ 'timestamp': time_stamp, 'temp': temp, 'flow': flow/7.5})        
    except Exception as ex:
        print('Exception', str(ex))
        pass
    time.sleep(1)
