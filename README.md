# Telegram Bot

El bot responderá a ciertos comandos para realizar acciones como encender/apagar leds, enviar la ubicación y obtener información del ambiente donde se encuentre instalado el dispositivo como son la humedad y la temperatura.

#### Materiales:
- Arduino Uno
- Protoboard
- Sensor DHT11
- Dos LED's
- Dos resistencias de 220 Ω
- Cable o Jumpers
#### Diagrama
![Diagrama](https://github.com/kubos777/alarmaBot/blob/master/alambrado.png)

#### Configuración del proyecto
Para correr el proyecto se necesita incluir la siguiente librería en arduino: 
```
#include "DHT.h"
```
En caso de no tenerla se puede descargar desde el gestor de librerías de arduino:
![DHT](https://github.com/kubos777/alarmaBot/blob/master/dht.png)

Y también necesitaremos las siguientes dos librerías:
![Unified](https://github.com/kubos777/alarmaBot/blob/master/unified.png)

Para Python, necesitamos instalar el modulo **pyserial** y **telepot** de la siguiente forma:
```
$ sudo pip3 install pyserial
$sudo pip3 install telepot
```