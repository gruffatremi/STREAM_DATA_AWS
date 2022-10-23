from time import time
import paho.mqtt.client as mqtt #pip install paho-mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
            print("Connected to MQTT Broker!")
    else:
            print("Failed to connect, return code %d\n", rc)

def on_message(client,userdata,msg):
    data=str(msg.payload.decode("utf-8"))
    print(msg.topic+" : "+data)

    #formatage_donnee(data)

    

def formatage_donnee(data):

    data_formater=data

    envoie_BDD(data_formater)

def envoie_BDD(data_formater):

    

    return 0

def main():

    client_id="12"
    broker="44.202.60.32"
    port_broker=1883
    topic="conso_elec"
    print("test")
    client=mqtt.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port_broker)
    
    client.subscribe(topic)
    client.on_message=on_message
    client.loop_forever()
    




if __name__ == "__main__":
    main()