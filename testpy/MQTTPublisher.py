import paho.mqtt.client as mqtt
import time 
import psutil as tramay
import subprocess
import re
from gpiozero import LED
from gpiozero import DigitalInputDevice
import adafruit_dht
import board
import pymysql

db,cur = None, None
db = pymysql.connect(host='192.168.137.152',user='root',password='iot1', db='giamsat')
#MQ2
MQ2=DigitalInputDevice(22)
#DHT11
dht11 = adafruit_dht.DHT11(board.D4, use_pulseio=False)
xanh = LED(18)
loa = LED(27)
# MQTT Broker thông tin
broker = "localhost"
port = 1883
topic = 'test/cpuwork'
topic1 = 'test/cputemperature'
topic2 = 'test/battat'
topic3 = 'test/ttden'
topic4 = 'test/dhttemp'
topic5 = 'test/dhthumd'
topic6 = 'test/baochay'
def docdoam():
    try:
        Do_C = dht11.temperature
        Do_F = Do_C * (9 / 5) + 32
        Doam = dht11.humidity
        return Do_C,Do_F,Doam
    except Exception as error:
        print(error)
        return None
    except RuntimeError as error:
        # Loi xay ra thuong xuyen con dht rat kho doc
        print(error.args[0])
        return None

def get_cpu_work():
    cpu_sd= tramay.cpu_percent(interval =1)
    return cpu_sd
    
def get_cpu_temperature():
    try:
        result = subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            # Lay ket quq tu stdout
            temp_output = result.stdout.strip()
            temp = re.findall(r'\d+\.\d+', temp_output)[0]
            return float(temp)
        else:
            print(f"Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None
# Hàm kết nối callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic2)
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")
    if message.payload.decode() == 'ON':
        client.publish(topic3,'Den Bat')
        xanh.on()
    elif message.payload.decode() =='OFF':
        client.publish(topic3,'Den Tat')
        xanh.off()
# Tạo một MQTT Client
client = mqtt.Client()

client.username_pw_set('iot1', 'iot1')
# Đăng ký hàm callback
client.on_connect = on_connect
client.on_message = on_message

# Kết nối đến Broker
client.connect(broker, port, 60)
# Duy trì kết nối
client.loop_start()
# Gửi một thông điệp đến topic
cur = db.cursor()
while 1:
    try:
        if docdoam() is not None :
            Do_C,Do_F,Doam = docdoam()
            sql2 = "INSERT INTO DHT11(nhietdo,doam) VALUES (%2.1f,%2.1f)" %(Do_C,Doam)
            cur.execute(sql2)
        elif docdoam() is None:
            Do_C=Doam=None
        if MQ2.value == 0:
            mq2_t = "Phat hien khi gas"
            loa.on()
        else:
            mq2_t = "Khong phat hien khi gas"
            loa.off()
        cpu_work = get_cpu_work()
        cpu_temperature = get_cpu_temperature()
        sql = "INSERT INTO Temp_Rasb(temperature) VALUES (%2.1f)" %cpu_temperature
        sql1 = "INSERT INTO Cpu_Load(cpu_load) VALUES (%2.1f)" %cpu_work
        client.publish(topic,'CPU load: {} %'.format(cpu_work))
        client.publish(topic1,f'Nhiet do Rasp: {cpu_temperature} *C')
        client.publish(topic4,f'{Do_C} *C')
        client.publish(topic5,f'{Doam} %')
        client.publish(topic6,f'{mq2_t} ')
        cur.execute(sql)
        cur.execute(sql1)
        db.commit()
        time.sleep(2)
    except Exception as error:
        raise error



