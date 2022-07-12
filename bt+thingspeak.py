import serial
import urllib.request as urllib

url = 'https://api.thingspeak.com/update?api_key=YOUR_KEY&field1={}'

with serial.Serial('/dev/cu.HC-05', 38400, timeout=1) as se: 
    while True:
        ret = se.read(100)
        if ret != b'':
            value = ret.decode('utf-8')
            urllib.urlopen(url.format(value))
            print(value)
