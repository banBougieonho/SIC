import time
import board
import adafruit_dht
from gpiozero import LED

xanh = LED(17)
loa = LED(27)
tbdht11 = adafruit_dht.DHT11(board.D22, use_pulseio=False)

def docdoam():
    try:
        Do_C = tbdht11.temperature
        Do_F = Do_C * (9 / 5) + 32
        Doam = dht11.humidity
        
    except Exception as error:
        tbdht11.exit()
        raise error
    except RuntimeError as error:
        # Loi xay ra thuong xuyen con dht rat kho doc
        print(error.args[0])
    return Do_C,Do_F,Doam
while 1:
    try:   
        Do_C,Do_F,Doam = docdoam()
        if 33 >= Do_C > 31:
            xanh.blink(on_time=1, off_time=1, n=None, background=1)
            loa.off()
            time.sleep(0.5)
        elif Do_C > 33:
            loa.blink(on_time=1, off_time=1, n=None, background=1)
            time.sleep(0.5)
        else:
            xanh.off()
            loa.off()
    except ValueError:
        print("Loi xu li du lieu tu dht11")
    except RuntimeError as error:
        # Loi xay ra thuong xuyen con dht rat kho doc
        print(error.args[0])
        time.sleep(2.0)
    time.sleep(5.0)
    
    
