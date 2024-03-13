import time
import json
import random
import paho.mqtt.client as paho
from dotenv import dotenv_values

config = dotenv_values()

# ----------------------
# Aquí crear los callbacks de MQTT
def on_connect_local(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt Local conectado")

        # Alumno: Suscribirse a los topicos locales deseados
        client.subscribe("sensores/gps")
        client.subscribe("sensores/inerciales")

    else:
        print(f"Mqtt Local connection faild, error code={rc}")


def on_connect_remoto(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt Remoto conectado")
    else:
        print(f"Mqtt Remoto connection faild, error code={rc}")

# Aquí crear el callback on_message (Puente de dato)
# ----------------------
def on_message_local(client, userdata, message):
    topico = message.topic
    mensaje = str(message.payload.decode("utf-8"))
    print(f"mensaje recibido {mensaje} en topico {topico}")

    topico_remoto = config["DASHBOARD_TOPICO_BASE"] + topico
    remoto = userdata["remoto"]
    remoto.publish(topico_remoto, mensaje)



if __name__ == "__main__":
    print("MQTT Local & Remoto")

    # ----------------------
    # Aquí conectarse a MQTT remoto
    client_remoto = paho.Client("gps_mock_remoto_danny_bracho")
    client_remoto.on_connect = on_connect_remoto
    client_remoto.username_pw_set(config["DASHBOARD_MQTT_USER"], config["DASHBOARD_MQTT_PASSWORD"])
    client_remoto.connect(config["DASHBOARD_MQTT_BROKER"], int(config["DASHBOARD_MQTT_PORT"]))
    client_remoto.loop_start()
    
    # Aquí conectarse a MQTT local
    client_local = paho.Client("gps_mock_local")
    client_local.on_connect = on_connect_local
    client_local.on_message = on_message_local
    client_local.user_data_set({"remoto":client_remoto})
    client_local.connect(config["BROKER"], int(config["PORT"]))
    client_local.loop_start()
   

    # ----------------------
    
    while True:
        pass
    
    # ----------------------

    client.disconnect()
    client.loop_stop()