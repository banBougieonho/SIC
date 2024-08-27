from gpiozero import LED
from gpiozero import MotionSensor
from gpiozero import DigitalInputDevice
from time import sleep

pir=MotionSensor(23)
#pik = DigitalInputDevice(22)
#red = LED(17)
#yl = LED(27)
#gr = LED(18)
print("Cho Motion khoi dong")
#pir.wait_for_no_motion()
"""for a in range(4):
    gr.on()
    red.on()
    yl.on()
    sleep(0.5)
    gr.off()
    red.off()
    yl.off()
    sleep(0.5)"""
while 1:
    print("Da san sang")
    if pir.wait_for_motion():
#    if pik.value == 1:
#       gr.blink()
        print("Phat hien chuyen dong")
    sleep(0.5)
#    if pir.wait_for_no_motion():
#    if pik.value ==0:
#        gr.off()
#        print("Null")
