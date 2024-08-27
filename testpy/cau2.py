import psutil
from gpiozero import LED
from time import sleep
from datetime import datetime

red = LED(17) #Do
yl = LED(27)  #Vang

baitap = open("/home/iot1/testpy/disk_usage_log.txt", "a")

while True:
    sudung= psutil.disk_usage('/').percent
    print(f"Dia dang su dung khoang: {sudung} %")
    # dieukhienled
    if sudung > 60:
        red.on()
        yl.off()
        print("RED bat")
    elif sudung > 30 and sudung <=60 :
        yl.on()
        red.off()
        print("Vang bat")
    else:
        red.off()
        yl.off()
        print("Dia duoi dung luong 30%")
    baitap.write(f"{datetime.now().strftime('%d/%m/%Y %HH %MM %SS')}: Dia da dung {sudung}%\n")
    sleep(5)
    baitap.close()


