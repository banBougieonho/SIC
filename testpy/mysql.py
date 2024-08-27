import subprocess
import re
import time
import pymysql
import psutil as tramay
db,cur = None, None

db = pymysql.connect(host='192.168.137.152',user='root',password='iot1', db='giamsat')

def get_cpu_work():
    cpu_sd= tramay.cpu_percent(interval =1)
    return cpu_sd
def get_cpu_temperature():
    try:
        result = subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            # L?y k?t qu? t? stdout
            temp_output = result.stdout.strip()
            temp = re.findall(r'\d+\.\d+', temp_output)[0]
            return temp
        else:
            print(f"Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

try:
    cur = db.cursor()
    while 1:
        cpu_work = get_cpu_work()
        cpu_temp = float(get_cpu_temperature())
        if cpu_temp is not None:
            sql = "INSERT INTO Temp_Rasb(temperature) VALUES (%2.1f)" %cpu_temp
            sql1 = "INSERT INTO Cpu_Load(cpu_load) VALUES (%2.1f)" %cpu_work
            print(f'{sql} \n\r{sql1}')
            cur.execute(sql)
            db.commit()
            cur.execute(sql1)
            db.commit()

        else:
            print("Failed to get CPU temperature")
        time.sleep(5)
except KeyboardInterrupt:
    print('Ket thuc!')
