from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DistanceSensor
from time import sleep

sensor=DistanceSensor(echo = 14,trigger = 15 , pin_factory= PiGPIOFactory())

gr = LED(22)

while 1:
    kc= sensor.distance * 100  
    #chuyen sang cm
    print("Khoang cach do dc: ",kc,"cm")
    if kc< 20:
        gr.on()
        print("Phat hien do vat")
    else:
        gr.off()
    sleep(1)
