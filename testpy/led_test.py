from math import *
from gpiozero import LED
from time import sleep

# Thử tạo một đối tượng LED (dù không có LED thực sự trên Windows)
led = LED(4)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
