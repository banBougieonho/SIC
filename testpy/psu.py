import psutil as tramay
from gpiozero import LED
from time import sleep
from datetime import *

while 1:
    cpu_sd= tramay.cpu_percent(interval =1, percpu=1)
    cpu_tb = sum([i/len(cpu_sd) for i in cpu_sd])
    cpu_tb = round(cpu_tb,3)
    print(f"Cpu dang sd: {cpu_sd}%")
    if 60 > cpu_tb > 30:
        print("Dang dung tren 30%")
    elif  cpu_tb >=60:
        print("Dang dung tren 60%")
    else:
        print("CPU hoat dong hoi nhan")

    data = f"{datetime.now().strftime('%Y /%m /%d %HH %MM %SS ')}" \
            f"Cpu su dung: {cpu_tb}% \n"
    with open("/home/iot1/baocaoraspi.txt", "a") as file:
        file.write(data)
    sleep(1)
