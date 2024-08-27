import Adafruit_DHT
import time

# Ch?n lo?i c?m bi?n (DHT11) v� ch�n GPIO
sensor = Adafruit_DHT.DHT11
pin = 4  # Ch�n GPIO 4 (BCM) tuong ?ng v?i ch�n v?t l� s? 7

def read_dht11():
    # �?c d? ?m v� nhi?t d? t? c?m bi?n DHT11
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    
    # Ki?m tra n?u vi?c d?c d? li?u th�nh c�ng
    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature:.1f}�C  Humidity: {humidity:.1f}%')
    else:
        print('Failed to get reading. Try again!')

print("Starting to read from DHT11 sensor...")

try:
    while True:
        read_dht11()
        time.sleep(2)  # �?c d? li?u m?i 2 gi�y
except KeyboardInterrupt:
    print("Program terminated.")
