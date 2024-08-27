import paho.mqtt.client as mqtt
import time
import psutil as tramay
# MQTT Broker thông tin
broker = "localhost"
port = 1883
topic = 'test/cpuwork'
topic1 = 'test/cputemperature'
# Hàm kết nối callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)
    client.subscribe(topic1)
    client.subscribe('test/battat')
def get_cpu_work():
    cpu_sd= tramay.cpu_percent(interval =1)
    return cpu_sd
# Hàm nhận thông điệp callback
def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

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
while 1:
    time.sleep(2)


