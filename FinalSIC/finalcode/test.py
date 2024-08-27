import adafruit_dht
import time
import board
#DHT11
dht11 = adafruit_dht.DHT11(board.D4, use_pulseio=False)
def docdoam():
    try:
        Do_C = dht11.temperature
        Do_F = Do_C * (9 / 5) + 32
        Doam = dht11.humidity
        return Do_C,Do_F,Doam
    except RuntimeError as error:
        # Loi xay ra thuong xuyen con dht rat kho doc
        print(error.args[0])
        return None
    except Exception as error:
        print(error)
        return None
    
while 1:
    try:
        if docdoam() is not None :
            Do_C,Do_F,Doam = docdoam()
        elif docdoam() is None:
            Do_C=Doam=None
        time.sleep(2)
    except Exception as error:
        raise error