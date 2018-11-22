import telepot, time,serial, sys
from serial import Serial
#ser = serial.Serial('COM10', 9600) Para WINDOWS
ser = serial.Serial('/dev/ttyACM0', 9600) #Para linux
print('¡El bot se ha activado!')
print('Esperando por comandos. . .')
def handle(msg):
        userName = msg['from']['first_name'] 
        content_type, chat_type, chat_id = telepot.glance(msg)
        #print(chat_id)  #Comprobamos el chat_id
        if (content_type == 'text'):
                command = msg['text']
                print ('Comando introducido: %s'%command)
                if  '/start' in command:
                        bot.sendMessage(chat_id, "Hola, "+userName+"\n"+"Hola, soy tochitoBot,la lista de comandos que puedo leer es:"+"\n"
                                        +"/encender_led1"+" * Prender led amarillo "+"\n"
                                        +"/apagar_led1"+" * Apagar led amarillo "+"\n"
                                        +"/encender_led2"+" * Prender led rojo"+"\n"
                                        +"/apagar_led2"+" * Apagar led rojo"+"\n"
                                        +"/ubicacion"+" * Ubicación de mi casa "+"\n"
                                        +"/humedad"+" * Medir la humedad de mi casa"+"\n"
                                        +"/temperatura"+" * Medir la temperatura de mi casa")
                elif '/encender_led1' in command:
                        ser.write(b'Y')
                        bot.sendMessage(chat_id, "¡Led amarillo prendido!")
                elif '/apagar_led1' in command:
                        ser.write(b'N')
                        bot.sendMessage(chat_id, "¡Led amarillo apagado!")
                elif '/encender_led2' in command:
                        ser.write(b'E')
                        bot.sendMessage(chat_id, "¡Led rojo prendido!")
                elif '/apagar_led2' in command:
                        ser.write(b'F')
                        bot.sendMessage(chat_id, "¡Led rojo apagado!")
                elif '/ubicacion' in command:
                        bot.sendLocation(chat_id, "Colocar latitud", "Colocar longitud")
                elif '/temperatura' in command:
                        ser.write(b'T')
                        linea = str(ser.readline())
                        linea = linea[2:-5]
                        temperatura = float(linea)
                        if temperatura >=40.0:
                            bot.sendMessage(chat_id,'¡Peligro, tu casa está en peligro')
                        else:
                            bot.sendMessage(chat_id, "Temperatura: %f °C"%temperatura) 
                elif '/humedad' in command:
                        ser.write(b'H')
                        linea=str(ser.readline())
                        linea = linea[2:-5]
                        humedad = float(linea)
                        bot.sendMessage(chat_id, 'Humedad relativa  %f '%humedad)
                else:
                    bot.sendMessage(chat_id, "¡Comando incorrecto!")
bot = telepot.Bot('Ingresar el token de tu bot')
bot.message_loop(handle)
# Esperando por nuevos mensajes
while 1:
    time.sleep(20)
 