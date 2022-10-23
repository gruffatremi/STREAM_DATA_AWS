import time
import paho.mqtt.client as mqtt #pip install paho-mqtt
import json
import requests
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import influxdb_client

token = "5up3r-S3cr3t-auth-t0k3n"
org = "influxdata-org"
bucket = "default"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
            print("Connected to MQTT Broker!")
    else:
            print("Failed to connect, return code %d\n", rc)

def on_message(client,userdata,msg):
    try:
        data=str(msg.payload.decode("utf-8"))
        print(msg.topic+" : "+data)
    except Exception as e:
        print(str(e))
    formatage_donnee(data)

def formatage_donnee(data):
    y = json.loads(data)
    print(y)
    # print(y["id"])
    # id = y['id']
    adresses = y['adresses']
    commune = y['commune']
    conso_elec = y['conso_elec']
    with InfluxDBClient(url="http://172.31.82.22:8086/", token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        p = influxdb_client.Point("default").tag("adresses", str(adresses)).tag("commune", str(commune)).tag("conso_elec", str(conso_elec)) .field("Null",str(id))

        write_api.write(bucket=bucket, org=org, record=p)

def main():

    client_id="12"
    #172.31.82.22
    broker="172.31.82.22"
    port_broker=1883
    topic="conso_elec"
    #CONNECT LOOP
    client=mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port_broker)
    print("Client connected")
    client.subscribe(topic)
    client.on_message=on_message
    while 1:
        try:
            client.loop_forever()
        except Exception as e:
            time.sleep(0.2)
            print(str(e))



if __name__ == "__main__":
    main()
