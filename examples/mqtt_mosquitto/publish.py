
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.


client = mqtt.Client()

client.on_connect = on_connect



client.connect("192.168.100.1", 1883, 60)

print client.publish("sensors/asd", "ASS121A")
