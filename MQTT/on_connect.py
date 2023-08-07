def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribe to a single topic for all parameters
    client.subscribe("strawberry/parameters")