from energy_prediction.print_predictions import *
from MQTT.manage_payload import *
import json

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