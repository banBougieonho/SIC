from gpiozero import Button
from gpiozero import LED
from time import sleep

touch = Button(16)
led = LED(15)
time=0
while 1:
    if touch.is_pressed == 1:
        print("LED OFF")
        while touch.is_pressed == 1:
            {}
    else:
        time=0
        print("LED ON")
        while touch.is_pressed == 0 :
            time = time+1
            if time == 5:
                print("DA doc duoc trang thai Nhan giu")
            sleep(1)
