from energy_prediction.print_predictions import *
from MQTT.update_via_mqtt import *
from image_analysis.detect_leaves import *
import threading

if __name__ == '__main__':
    # Create a thread for the update_via_mqtt function
    mqtt_thread = threading.Thread(target=update_via_mqtt)

    try:
        # Start the thread
        mqtt_thread.start()
    except: 
        print("Could not start MQTT thread.")

    # Continue with the rest of the program
    print_predictions()
    detect_leaves('/mnt/c/strawberries/Strawberry___Healthy')

    try:
        # Wait for the mqtt_thread to finish before exiting the program
        mqtt_thread.join()
    except:
        print("Could not access MQTT thread")