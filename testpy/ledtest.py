from gpiozero import LED
from time import sleep
from signal import *
# Thử tạo một đối tượng LED (dù không có LED thực sự trên Windows)
led = LED(17)
while 1:
    led.blink(on_time=0.5, off_time=0.5, n=None, background=False)
