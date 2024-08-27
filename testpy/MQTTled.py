import paho.mqtt.client as mqtt
import time 
from gpiozero import LED
from gpiozero import DigitalInputDevice
from signal import pause
auto = 1

#output
phongkhach = LED(18)
bep = LED(21)
ngu = LED(20)

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

topic11 = 'phongkhach/battatbancong'
topic12 = 'phongkhach/ttdenbancong'
topic13 = 'phongkhach/battatbep'
topic14 = 'phongkhach/ttdenbep'
topic15 = 'phongkhach/battatngu'
topic16 = 'phongkhach/ttdenngu'

# Hàm kết nối callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic2)
    client.subscribe(topic13)
    client.subscribe(topic15)

def on_message(client, userdata, message):
    global auto
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")
    if message.payload.decode() == 'ON':
        client.publish(topic3,'Den Bat')
        phongkhach.on()
    elif message.payload.decode() =='OFF':
        client.publish(topic3,'Den Tat')
        phongkhach.off()
    elif message.payload.decode() =='ONNGU':
        client.publish(topic16,'Den Bat')
        ngu.on()
    elif message.payload.decode() =='OFFNGU':
        client.publish(topic16,'Den Tat')
        ngu.off()
    elif message.payload.decode() =='ONBEP':
        client.publish(topic14,'Den Bat')
        bep.on()
    elif message.payload.decode() =='OFFBEP':
        client.publish(topic14,'Den Tat')
        bep.off()
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
bep.off()
ngu.off()
client.publish(topic14,'Den Tat')
client.publish(topic16,'Den Tat')
while 1:
    {}

