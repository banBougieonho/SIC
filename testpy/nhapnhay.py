from gpiozero import LED
from time import sleep

red = LED(17)
yl = LED(27)
gr = LED(22)

gr.on()
red.off()
yl.off()
while 1:
    sleep(2)
    gr.off()
    yl.on()
    sleep(2)
    red.on()
    yl.off()
    sleep(2)
    red.off()
    yl.on()
