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


def publish(client,topic,response):

    for i in range(40):
        adresses = response.json()['values'][i]['adresses']
        commune = response.json()['values'][i]['commune']
        conso_elec = str(response.json()['values'][i]['conso_elec'])
        time.sleep(1)
        #dico_secteur="{"+"adresses : "+data.json()['values'][i]["adresses"]+", commune : "+data.json()['values'][i]["commune"]+", conso_elec : "+str(data.json()['values'][i]["conso_elec"])+"}"
        dictionnaire= {"adresses":adresses,"commune":commune,"conso_elec":conso_elec}
        # secteur="test"+str(i)
        # print (dico_secteur)
        print(str(dictionnaire))
        jsonStr = json.dumps(dictionnaire)
        data_str = str(jsonStr)
        print(data_str)
        time.sleep(1)
        result = client.publish(topic, data_str)
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

    broker = '172.31.82.22'
    port = 1883
    topic = "conso_elec"

    client_id = "1"

    client = mqtt_client.Client(client_id)

    client.on_connect = on_connect
    client.connect(broker, port)
    while 1:
        response = requests.get('https://download.data.grandlyon.com/ws/rdata/nrj_energie.nrjcad_parcelles_2018/all.json?maxfeatures=100&start=1&ds=,&separator=;%27')
        publish(client,topic,response)
        time.sleep(1)


if __name__ == '__main__':
    main()

