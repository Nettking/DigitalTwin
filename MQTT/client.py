from MQTT.on_connect import on_connect
from MQTT.on_message import on_message
import paho.mqtt.client as mqtt

def client():
    client_ip = '127.0.0.1'
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    return client, client_ip