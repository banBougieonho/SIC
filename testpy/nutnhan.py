from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause
red = LED(17)
yl = LED(27)
gr = LED(22)
nhan = Button(14)
for a in range(4):
    gr.on()
    red.on()
    yl.on()
    sleep(0.5)
    gr.off()
    red.off()
    yl.off()
    sleep(0.5)
i=0
while 1:
    if nhan.is_pressed:
        while nhan.is_pressed:
           {} 
        i+=1
        print("Nut da duoc nhan",i)
    if i==0:
        red.blink()
    elif i==1:
        yl.blink()
    
    elif i == 2:
        gr.blink()
    
    elif i==3:
        red.blink()
        yl.blink()
        gr.blink()
    
    elif i == 4:
        i=0
