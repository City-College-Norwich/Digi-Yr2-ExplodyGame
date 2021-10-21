import time
import network
import urequests as requests
        


class Wifi:
    wlan = None
    SSID = "OrnamentNet"        
    PASSWORD = "ItsSoPretty"
    URL = "http://192.1.1.1:5000/"

    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

        self.wlan.connect(self.SSID, self.PASSWORD)

        while True:
            if self.wlan.isconnected():
                print ("Connected to: " + self.SSID)
                return
            time.sleep_ms(500)
            print ("Connecting")
    
    def sendRequest(self, message):
        response = requests.get(self.URL + message)
        text = response.text
        if response.statusCode != 200:
            text = ""
        response.close()
        return text
