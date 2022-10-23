import time
import requests #py -m pip install requests
import json
import time

from paho.mqtt import client as mqtt_client     #pip install paho-mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


def publish(client,topic,data):

    for i in range(10):

        time.sleep(1)
        dico_secteur = data.json()['values'][i]
        secteur="test"+str(i)
        print (secteur)
        time.sleep(1)
        result = client.publish(topic, secteur)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print("Data envoyé")
        else:
            print("Echec")


def main():

    #Recup des données de l'API

    response = requests.get('https://download.data.grandlyon.com/ws/rdata/nrj_energie.nrjcad_parcelles_2018/all.json?maxfeatures=100&start=1&ds=,&separator=;%27')

    #Publish sur le broker

    broker = '44.202.60.32'
    port = 1883
    topic = "conso_elec"

    client_id = "1"

    client = mqtt_client.Client(client_id)

    client.on_connect = on_connect
    client.connect(broker, port)
    
    client.loop_start()
    publish(client,topic,response)
    client.loop_stop()


if __name__ == '__main__':
    main()





    