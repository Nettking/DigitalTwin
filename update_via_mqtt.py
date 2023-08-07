import paho.mqtt.client as mqtt
import json
from predictions import *



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribe to a single topic for all parameters
    client.subscribe("strawberry/parameters")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))

    param_name = payload["parameter"]
    param_value = payload["value"]

    if param_name == "hours_active_lights":
        global hours_active_lights
        hours_active_lights = float(param_value)

    elif param_name == "hours_active_computer":
        global hours_active_computer
        hours_active_computer = float(param_value)

    elif param_name == "hours_active_irrigations":
        global hours_active_irrigations
        hours_active_irrigations = float(param_value)

    elif param_name == "watt_pr_hour_lights":
        global watt_pr_hour_lights
        watt_pr_hour_lights = float(param_value)

    elif param_name == "watt_pr_hour_computer":
        global watt_pr_hour_computer
        watt_pr_hour_computer = float(param_value)

    elif param_name == "watt_pr_hour_irrigations":
        global watt_pr_hour_irrigations
        watt_pr_hour_irrigations = float(param_value)

    elif param_name == "total_watt_pr_day_lights":
        global total_watt_pr_day_lights
        total_watt_pr_day_lights = float(param_value)

    elif param_name == "total_watt_pr_day_computer":
        global total_watt_pr_day_computer
        total_watt_pr_day_computer = float(param_value)

    elif param_name == "total_watt_pr_day_irrigations":
        global total_watt_pr_day_irrigations
        total_watt_pr_day_irrigations = float(param_value)

    elif param_name == "average_total_watt_consumption":
        global average_total_watt_consumption
        average_total_watt_consumption = float(param_value)

    elif param_name == "days_of_cultivation":
        global days_of_cultivation
        days_of_cultivation = float(param_value)

    elif param_name == "total_energy_consumption":
        global total_energy_consumption
        total_energy_consumption = float(param_value)

    elif param_name == "price_of_energy_pr_kilo_watt":
        global price_of_energy_pr_kilo_watt
        price_of_energy_pr_kilo_watt = float(param_value)

    elif param_name == "total_cultication_price":
        global total_cultication_price
        total_cultication_price = float(param_value)

    elif param_name == "expected_yield_pr_plant":
        global expected_yield_pr_plant
        expected_yield_pr_plant = float(param_value)

    elif param_name == "weight_pr_strawberry":
        global weight_pr_strawberry
        weight_pr_strawberry = float(param_value)

    elif param_name == "number_of_pots":
        global number_of_pots
        number_of_pots = int(param_value)

    elif param_name == "number_of_strawberries":
        global number_of_strawberries
        number_of_strawberries = int(param_value)

    elif param_name == "price_pr_strawberry":
        global price_pr_strawberry
        price_pr_strawberry = float(param_value)
    print('Parameter ' + param_name + ' updated via MQTT. Running prediction with new parameters.')
    print_predictions(hours_active_lights, hours_active_computer, hours_active_irrigations, watt_pr_hour_lights, watt_pr_hour_computer, watt_pr_hour_irrigations, total_watt_pr_day_lights, total_watt_pr_day_computer, total_watt_pr_day_irrigations, average_total_watt_consumption, days_of_cultivation, total_energy_consumption, price_of_energy_pr_kilo_watt, total_cultication_price, expected_yield_pr_plant, weight_pr_strawberry, number_of_pots, number_of_strawberries, price_pr_strawberry)


client_ip = '127.0.0.1'
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(client_ip, 1883, 60) # Replace with your broker's address and port

client.loop_forever()