import urequests as requests
import ujson

class Cloud:
    def __init__(self, url:str):
        self.url = url
    
    def sendData(self, data):
        print('sendData')
        post_data = ujson.dumps(data)      
        resp = requests.post(self.url, headers = {'content-type': 'application/json'}, data = post_data).json()
        print(resp)