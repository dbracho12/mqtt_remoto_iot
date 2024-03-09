import time
import json
import random
import paho.mqtt.client as paho
from dotenv import dotenv_values

config = dotenv_values()

# ----------------------
# Aquí crear los callbacks de MQTT
def on_connect(client, userdata, flags,rc):
    if rc == 0:
        print("Me conecte")
    else:
        print("Fallo la conexion") 

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
    for i in range(20):
        data["longitude"] +=.0001
        json_str = json.dumps(data)
        client.publish(topico,json_str)
        time.sleep(2)
    # ----------------------
    client.disconnect()
    client.loop_stop()
    # conectarle al MQTT Explore
