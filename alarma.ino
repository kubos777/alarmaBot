
#include "DHT.h" //Libreria DHT para el control de el Sensor DHT 11
#define PinOutDHT 3 //Definimos el pin 3 para la lectura del sensor
#define TypeDHT DHT11 //Definimos el tipo de Sensor.
DHT dht(PinOutDHT, TypeDHT); //Objeto de tipo DHT con las características anteriores
const int led1=12; //Led 1
const int led2=2; //Led 2
unsigned int dato; //Para guardar los valores recibidos desde Python
void setup() {
  Serial.begin(9600); //Iniciando comunicación serial
  pinMode(led1,OUTPUT); //Modo de salida para los LEDs
  pinMode(led2,OUTPUT); 
  
}
void loop() {
    while(Serial.available()>0){  
      dato=Serial.read(); //Se lee el puerto serial y guarda los valores en la variable dato    
      //Para prender o apagar los leds, según el comando recibido desde Python
        if(dato=='Y')digitalWrite(led1,HIGH);
        if(dato=='N')digitalWrite(led1,LOW);
        if(dato=='E')digitalWrite(led2,HIGH);
        if(dato=='F')digitalWrite(led2,LOW);
      //Para mandar temperatura y humedad
        if(dato=='T')Serial.println(int(dht.readTemperature()));
        if(dato=='H')Serial.println(int(dht.readHumidity()));
        if(dato=='B'){
        }
    }
}
