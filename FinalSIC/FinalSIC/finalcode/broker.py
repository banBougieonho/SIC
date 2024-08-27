import paho.mqtt.client as mqtt
broker = "192.168.137.152"
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
topic11 = 'phongkhach/battatbancong'
topic12 = 'phongkhach/ttdenbancong'
topic13 = 'phongkhach/battatbep'
topic14 = 'phongkhach/ttdenbep'
topic15 = 'phongkhach/battatngu'
topic16 = 'phongkhach/ttdenngu'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)
    client.subscribe(topic1)
    client.subscribe(topic2)
    client.subscribe(topic3)
    client.subscribe(topic4)
    client.subscribe(topic5)
    client.subscribe(topic6)
    client.subscribe(topic7)
    client.subscribe(topic8)
    client.subscribe(topic9)
    client.subscribe(topic11)
    client.subscribe(topic12)
    client.subscribe(topic13)
    client.subscribe(topic14)
    client.subscribe(topic15)
    client.subscribe(topic16)

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

def main():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(broker, port)
    mqtt_client.loop_forever()

if __name__ == '__main__':
    main()
