import paho.mqtt.client as mqtt
import time 
import psutil as tramay
import subprocess
import re
from gpiozero import LED
from gpiozero import DigitalInputDevice
from gpiozero import DigitalOutputDevice
import adafruit_dht
import board
import pymysql
auto = 1
db,cur = None, None
db = pymysql.connect(host='192.168.137.152',user='root',password='iot1', db='giamsat')
#DHT11
dht11 = adafruit_dht.DHT11(board.D4, use_pulseio=False)
#output
#relay
relay = DigitalOutputDevice(26)
# MQTT Broker thông tin
broker = "localhost"
port = 1883
topic = 'pi/cpuwork'
topic1 = 'pi/cputemperature'
topic2 = 'phongkhach/battat'
topic3 = 'phongkhach/ttden'
topic4 = 'phongkhach/dhttemp'
topic5 = 'phongkhach/dhthumd'
topic6 = 'phongkhach/baochay'
topic7 = 'phongkhach/ttquat'
topic8 = 'phongkhach/tudongquat'
topic9 = 'phongkhach/battatquat'

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
    client.subscribe(topic8)
    client.subscribe(topic9)

def on_message(client, userdata, message):
    global auto
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")
    if message.payload.decode() =='quatonauto':
        auto = 1
    elif message.payload.decode() =='quatoffauto':
        auto = 0
    elif message.payload.decode() =='quatoff':
        relay.off()
        client.publish(topic7,'Quat off')
    elif message.payload.decode() =='quaton':
        relay.on()
        client.publish(topic7,'Quat bat')
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
            if Do_C >=30 and auto == 1:
                relay.on()
                client.publish(topic7,'Quat bat')
            elif Do_C <30 and auto == 1:
                relay.off()
                client.publish(topic7,'Quat tat')
        elif docdoam() is None:
            Do_C=Doam=None
        cpu_work = get_cpu_work()
        cpu_temperature = get_cpu_temperature()
        sql = "INSERT INTO Temp_Rasb(temperature) VALUES (%2.1f)" %cpu_temperature
        sql1 = "INSERT INTO Cpu_Load(cpu_load) VALUES (%2.1f)" %cpu_work
        client.publish(topic,'CPU load: {} %'.format(cpu_work))
        client.publish(topic1,f'Nhiet do Rasp: {cpu_temperature} *C')
        client.publish(topic4,f'{Do_C} *C')
        client.publish(topic5,f'{Doam} %')
        cur.execute(sql)
        cur.execute(sql1)
        db.commit()
        time.sleep(2)
    except Exception as error:
        raise error



