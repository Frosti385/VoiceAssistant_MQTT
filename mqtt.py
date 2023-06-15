import paho.mqtt.client as mqtt;

client_id = "xeroVA";
client = mqtt.Client(client_id);
local_broker_address = "openhabian";

def mqtt_publish(topic, payload):
    client.connect(local_broker_address); #Abfrage, ob verbindung erfolgt

    client.publish(topic, payload)

    return True;

client.connect(local_broker_address);




