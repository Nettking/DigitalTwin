from energy_prediction.print_predictions import *
from MQTT.update_via_mqtt import *
from image_analysis.detect_leaves import *
import threading

if __name__ == '__main__':
    try:
        # Create a thread for the update_via_mqtt function
        mqtt_thread = threading.Thread(target=update_via_mqtt)
        print("MQTT thread created.")
    except: 
        print("Couldn't create thread for update_via_mqtt.")
    
    try:
        # Start the thread
        mqtt_thread.start()
        print("MQTT thread started")
    except: 
        print("Could not start MQTT thread.")

    # Continue with the rest of the program
    try:
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
    except:
        print("Could not print predictions")
    
    try:
        detect_leaves('/mnt/c/strawberries/Strawberry___Healthy')
    except:
        print("Could not detect leaves")

    try:
        # Wait for the mqtt_thread to finish before exiting the program
        mqtt_thread.join()
    except:
        print("Could not access MQTT thread")