import time
import json
import random
import paho.mqtt.client as paho
from dotenv import dotenv_values

config = dotenv_values()

# ----------------------
# Aquí crear los callbacks de MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt Publicador conectado")
    else:
        print(f"Mqtt Publicador connection faild, error code={rc}")

# ----------------------


if __name__ == "__main__":
    print("GPS Mock: Sensor de posicionamiento gloal")

    # ----------------------
    # Aquí conectarse a MQTT
    client = paho.Client("gps_mock_local")
    client.on_connect = on_connect
    client.connect(config["BROKER"], int(config["PORT"]))
    client.loop_start()

    # ----------------------
    
    # Datos iniciales
    topico = "sensores/gps"
    data = {"latitude": -34.55, "longitude": -58.498}

    # ----------------------
    # Aquí preparar el blucle para enviar datos
    for i in range(4000):
        data["longitude"] += .0001
        data_jsonstr = json.dumps(data)
        ret = client.publish(topico, data_jsonstr) 
        time.sleep(.1)
    
    # ----------------------

    client.disconnect()
    client.loop_stop()