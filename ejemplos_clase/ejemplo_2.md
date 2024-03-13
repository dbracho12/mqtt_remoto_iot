cd# Ejemplos de clase

En esta práctica utilizaremos el simulador "drone_iot" con de celular para obtener valores de sensores reales informados por el celular.

En caso que usted no desee user o no pueda usar el simulador "drone_iot" junto a su celular, puede utilizar el simulador "sensores_mock" que se introducirá en otra práctica. 

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Preparar el entorno de trabajo

Abrir el Visual Studio Code y conectarse de forma remota al dispositivo. Trabajaremos sobre la carpeta recientemente clonada de este repositorio.

Clonar el repositorio del simulador de sensores:
```sh
$ git clone https://github.com/InoveAlumnos/drone_iot
```

Topicos que soporta que utilizaremos de este mock:
|             |             | datos ejemplo
| ----------  | --------    | -----
|  sensores   | gps         | {"latitude": -34.55, "longitude": -58.496}
|  sensores   | inericiales | {"heading": 160, accel: 4.5}


### 2 - Lanzar el simulador drone iot
Desde ssh conectado a la VM, ingresar a la carpeta clonada del "drone_iot" y lanzar la aplicación:
```sh
$ python3 app.py
```

Ingresar a su explorador web e ingresar a al aplicación del drone. Recuerde ingresar con la URL en https y aceptar el ingreso "inseguro" a la app.
```
https://<ip_VM>:5010
```

### 3 - Ensayar que el simulador funcione
Utilizar el MQTTExplorar y verificar de esta manera el correcto funcionamiento de cada sensor disponible del celular.

Ejemplo de visualización de los cambios de aceleración:
![ejemplo_2](ejemplo_2.png)
