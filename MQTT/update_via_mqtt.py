from energy_prediction.print_predictions import *
from MQTT.manage_payload import *
import MQTT.client

def update_via_mqtt():
    client, client_ip = MQTT.client.client()

    client.connect(client_ip, 1883, 60)

    client.loop_forever()