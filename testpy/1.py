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


cham = Button(16)
xanh = LED(17)
loa = DigitalOutputDevice(27)
tbdht11 = adafruit_dht.DHT11(board.D4,use_pulseio=False)

bien = 0
def docdoam():
    try:
        Do_C = tbdht11.temperature
        Do_F = Do_C * (9 / 5) + 32
        Doam = tbdht11.humidity
        hienthi = "Nhiet do: {:.1f} F / {:.1f} C  \r\nDo am: {}% ".format(Do_F, Do_C, Doam)
        print(hienthi)
    except ValueError:
        print("Loi xu li du lieu tu dht11")
    except RuntimeError as error:
        # Loi xay ra thuong xuyen con dht rat kho doc
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
       {}
    time.sleep(5.0)
    return Do_C,Do_F,Doam

def luufile(data):
    with open("bcnhietdo.txt","a") as file:
        file.write(data)

while 1:
    try:
        if cham.is_pressed == 0:
            dem=0
            print("Phat hien cham")
            while cham.is_pressed ==0:
                dem =dem+1
                time.sleep(0.5)
                if dem < 5:
                    print("Chua cham du ")
                if dem >= 5:
                    print("Cham du ")
                    bien=bien+1
                    if bien >=256:
                        bien=0
                    loa.on()
                    time.sleep(1)
                    loa.off()

        if bien%2 != 0:
            try:
                DoRas = subprocess.run(['vcgencmd', 'measure_temp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                Do_C,Do_F,Doam = docdoam()
    
                if 33 >= Do_C > 31:
                    xanh.blink(on_time=1, off_time=1)
                    loa.off()
                    time.sleep(0.5)
                elif Do_C > 33:
                    loa.blink(on_time=0.2, off_time=1)
                    xanh.on()
                    time.sleep(0.5)
                else:
                    xanh.off()
                    loa.off()
                data = f"\r\n{datetime.now().strftime('%Y /%m /%d %HH %MM %SS ')} - Nhiet do Ras: {DoRas.stdout}"
                luufile(data)
                hienthi = "Nhiet do: {:.1f} F / {:.1f} C -- Do am: {}% \n".format(Do_F, Do_C, Doam)
                luufile(hienthi)
            except Exception as error:
                print("Co loi vui long cho!")
        else:
            print("Cham de bat")
            time.sleep(2)
            loa.off()
            xanh.off()
        
    except KeyboardInterrupt:
        loa.close()
        tbdht11.close()


    
