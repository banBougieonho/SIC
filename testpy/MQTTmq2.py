import paho.mqtt.client as mqtt
import time 
from gpiozero import LED
from gpiozero import DigitalInputDevice
import pymysql

#DataBase
db = pymysql.connect(host='192.168.137.152',user='root',password='iot1', db='giamsat')
cur = db.cursor()
#MQ2
MQ2=DigitalInputDevice(22)
#Output Devices
loa = LED(27)
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

# Hàm kết nối callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic2)
# Hàm nhận tin  
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Tạo một MQTT Client
client = mqtt.Client()
# user passwd MQTT Client
client.username_pw_set('iot1', 'iot1')

# Đăng ký hàm callback
client.on_connect = on_connect
client.on_message = on_message

# Kết nối đến Broker
client.connect(broker, port, 60)
# Duy trì kết nối
client.loop_start()
# Gửi một thông điệp đến topic

while 1:
    try:
        if MQ2.value == 0:
            mq2_t = 'Phat hien khi gas'
            loa.blink(on_time=0.5, off_time=0.2)
        else:
            mq2_t = 'Khong phat hien khi gas'
            loa.off()
        cur.execute(f"INSERT INTO MQ2_caution(Infor) VALUES ('{mq2_t}')")
        client.publish(topic6,f'{mq2_t} ')
        db.commit()
        time.sleep(2)

    except Exception as error:
        raise error
