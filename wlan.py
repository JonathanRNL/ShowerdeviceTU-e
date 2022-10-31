#ShowerBud Team 105
import network
import time


class Wlan:
    def __init__(self):
       self.station = network.WLAN(network.STA_IF) 
       self.station.active(True)
       print('Wlan ready')

    def scan(self):
        print('Scanning networks')
        return self.station.scan()
    
    def connect(self, ssid:str, password:str) -> None:
        print('Connecting...')
        for attempt in range(1, 10):
            try:
                print('Connect attempt', attempt)
                self.station.connect(ssid, password)
            except:
                pass
            if self.station.isconnected():
                break
            time.sleep(1)
    
    def disconnect(self) -> None:        
        try:     
            self.station.disconnect()
        except:
            pass
        self.station.active(True)        
        time.sleep(1)
        
    def printNetworks(self) -> None:
        networks = self.scan()
        for nw in networks:
             print(nw)
