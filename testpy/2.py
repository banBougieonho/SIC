import time
import board
import subprocess
import adafruit_dht
from gpiozero import LED
from gpiozero import Button
from gpiozero import MotionSensor
from datetime import datetime
from gpiozero import DigitalInputDevice
from gpiozero import DigitalOutputDevice


MQ2 = DigitalInputDevice(26)
vang = LED(23)
loachay = DigitalOutputDevice(24)
cdong = DigitalInputDevice(22)


while 1:
        if MQ2.value == 0:
            print("Phat hien gas!")
            loachay.blink(on_time=0.2,off_time=0.1)
        else:
            loachay.off()
        if cdong.value!=0:
            print("Phat hien chuyen dong")
            vang.blink()
        else:
            vang.off()
       