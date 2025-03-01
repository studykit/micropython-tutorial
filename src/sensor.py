from machine import Pin
import dht

# DHT11 센서 설정
_sensor = dht.DHT11(Pin(16))  # D0 핀은 GPIO16에 해당

def read():
    _sensor.measure()
    temp = _sensor.temperature()
    hum = _sensor.humidity()
    return temp, hum
