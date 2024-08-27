import paho.mqtt.client as mqtt
import time 
from gpiozero import LED
from gpiozero import DigitalInputDevice

#Motion PIR
pir = DigitalInputDevice(16)
#Output Devices
bancong = LED(17)
# MQTT Broker thông tin
broker = "192.168.137.152"
port = 1883
topic = 'pi/cpuwork'
topic1 = 'pi/cputemperature'
topic2 = 'phongkhach/battat'
topic3 = 'phongkhach/ttden'
topic4 = 'phongkhach/dhttemp'
topic5 = 'phongkhach/dhthumd'
topic6 = 'phongkhach/baochay'
topic7 = 'phongkhach/motiondetect'
topic8 = 'phongkhach/motiondetectonoff'
topic11 = 'phongkhach/battatbancong'
topic12 = 'phongkhach/ttdenbancong'
key = "on"
bancong.off()
# Hàm kết nối callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic8)
    client.subscribe(topic11)
# Hàm nhận tin  
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")
    global key
    if message.payload.decode() == '1':
        key = "on"
    elif message.payload.decode() == '0':
        key = "off"    
    elif message.payload.decode() == 'ONBC':
        client.publish(topic12,'Den Bat')
        bancong.on()
    elif message.payload.decode() == 'OFFBC':
        client.publish(topic12,'Den Tat')
        bancong.off()    
        
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

while 1:
    try:
        last_motion_time = 0  
        while key == "on":
            if time.time() - last_motion_time > 180:
                print("Không phát hiện chuyển động trong 3 phút. Tắt đèn.")
                pir_st = 'Not detect'
                bancong.off()
                client.publish(topic12,'Den Tat')
            if pir.value == 1:
                bancong.on()
                print("Phát hiện chuyển động!")
                last_motion_time = time.time()  # Cập nhật
                pir_st = 'Detect'
                client.publish(topic12,'Den Bat')
            client.publish(topic7,f'{pir_st}')
            time.sleep(1)  # Chờ 1 giây 
    except Exception as error:
        raise error
