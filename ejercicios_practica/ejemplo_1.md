# Ejercicios de práctica

En esta práctica utilizaremos el simulador "actuadores_mock" junto a la librería de Paho MQTT

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Preparar el entorno de trabajo

Abrir el Visual Studio Code y conectarse de forma remota al dispositivo. Trabajaremos sobre la carpeta recientemente clonada de este repositorio.

Clonar el repositorio del simulador de actuadores:
```sh
$ git clone https://github.com/InoveAlumnos/actuadores_mock_iot
```

Topicos que soporta este mock drone emulado:
|             |          |      | datos ejemplo
| ----------  | -------- | -----| -----
|  actuadores | luces    | 1    |  0/1
|  actuadores | volar    |      |  0/1
|  actuadores | motores  | 1..4 |  0/1
|  actuadores | joystick |      |  {"x": 0.8, "y": 0.3}


### 2 - Lanzar el simulador sensores mock
Desde ssh conectado a la VM, ingresar a la carpeta clonada del "actuadores_mock_iot" y lanzar la aplicación:
```sh
$ python3 app.py
```

Ingresar a su explorador web e ingresar a al aplicación del drone:
```
http://<ip_VM>:5007
```

### 3 - Ensayar que el simulador funcione
Utilizar el MQTTExplorar y verificar de esta manera el correcto funcionamiento de cada actuador disponible. 


### 4 - Script capturador de actuadores
Dentro de la carpeta "ejercicios_practica" cree un script llamado "ejercicio_1". En dicho script deberá crear dos clientes MQTT --> uno local y otro remoto. Tal cual se vio en clase, arme el script utilizando las variable de entorno en el archivo ".env" (modifique su usuario del cmapus) y conectese al MQTT local (su VM) y al remoto (dashboard.)

Dentro de la función "on_connect_local" agregar las lineas requeridas para suscribirse a los tópicos de los actuadores:
```python
client.subscribe("actuadores/luces/1")
client.subscribe("actuadores/volar")
etc etc etc
```

Crear la función de "on_message" que utilizaremos para capturar los mensajes que llegan a los topicos suscriptos al MQTT local:
```python
def on_message(client, userdata, message):
    topico = message.topic
    mensaje = str(message.payload.decode("utf-8"))
    print(f"mensaje recibido {mensaje} en topico {topico}")
```

### 5 - Enviar datos a remoto
Antes de comenzar, editar el archivo .env la variable "DASHBOARD_TOPICO_BASE" con su usuario de alumno del campus.

Agregar la variable de "cliente_remoto" dentro de las "user_data" del cliente local, utilizando "user_data_set":
```python
client_local = paho.Client("gps_mock_local")
client_local.on_connect = on_connect_local
client_local.on_message = on_message
client_local.user_data_set({"client_remoto": client_remoto})
```

En la función "on_message" obtener nuevamente la variable "cliente_remoto" de "user_data":
```python
client_remoto = userdata["client_remoto"]
```

Enviar el dato recibido en "on_message" al MQTT remoto, transformando el tópico agregando "DASHBOARD_TOPICO_BASE" al comienzo del tópico recibido.
```python
topico_remoto = config["DASHBOARD_TOPICO_BASE"] + topico
client_remoto.publish(topico_remoto, mensaje)
```

Si todo funciona correctamente, en el dashboard deberá ver como la luz y los motores se encienden o se apagan según lo que usted haga en la aplicación de "actuadores_mock".

Utilice todas las herramientas a su disposición (terminal, MQTTExplorer, debugger) para ensayar y testear el funcionamiento de su implementación. En caso que tenga problemas, consulte y continue explorando. Lo más rico de estos ejercicios es que pueda analizar las fallas y aprender de ellas por su cuenta como todo un buen detective.

Una vez finalizado el ejercicio y corroborado el funcionamiento, subir al repositorio el script de python resuelto de este ejercicio en la carpeta de "ejercicios_practica" con el nombre de "ejercicio_1.py".
