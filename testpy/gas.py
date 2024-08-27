from gpiozero import DigitalInputDevice
from gpiozero import DigitalOutputDevice
import time

MQ2 = DigitalInputDevice(26)
loa = DigitalOutputDevice(24)
while True:

    if MQ2.value == 0:
        print("Gas phat hien!")
        loa.blink()
    else:
        print("Khong phat hien Gas")
        loa.off()
    
    time.sleep(1)