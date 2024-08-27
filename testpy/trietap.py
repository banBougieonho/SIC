import time
from gpiozero import *
from gpiozero import LED
from gpiozero import Buzzer
pot = MCP3008(0)

xanh = LED(19)
loa = Buzzer(26)
while True:
    print(round(pot.value * 250,3),"V")
    while pot.value*250>= 210:
        print("Densang")
    else:
        print("dentat")
        xanh.off()
        loa.off()
    time.sleep(2)

