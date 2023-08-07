import paho.mqtt.client as mqtt
from energy_prediction.print_predictions import *
from MQTT.manage_payload import *
from MQTT.on_connect import on_connect
from MQTT.on_message import on_message

def update_via_mqtt():
    client_ip = '127.0.0.1'
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(client_ip, 1883, 60)

    client.loop_forever()