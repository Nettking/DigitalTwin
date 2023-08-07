import paho.mqtt.client as mqtt
import json
from print_predictions import *
from manage_payload import *

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribe to a single topic for all parameters
    client.subscribe("strawberry/parameters")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))
    param_name = manage_payload(payload)
    print('Parameter ' + param_name + ' updated via MQTT. Running prediction with new parameters.')
    print_predictions(hours_active_lights, 
                      hours_active_computer, 
                      hours_active_irrigations, 
                      watt_pr_hour_lights, 
                      watt_pr_hour_computer, 
                      watt_pr_hour_irrigations, 
                      days_of_cultivation, 
                      price_of_energy_pr_kilo_watt, 
                      expected_yield_pr_plant, 
                      weight_pr_strawberry, 
                      number_of_pots)

def update_via_mqtt():
    client_ip = '127.0.0.1'
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(client_ip, 1883, 60)

    client.loop_forever()