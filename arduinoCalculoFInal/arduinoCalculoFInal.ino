#include <Wire.h>
#include "Adafruit_TCS34725.h"
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1 
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
Adafruit_TCS34725 tcs = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);

const int redPin = 11;
const int greenPin = 10;
const int bluePin = 9;

void setup(){
  Serial.begin(115200);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  setColor(0, 0, 0); 

  if(!tcs.begin()){
    Serial.println("No se encuentra sensor");
    while (1);
  }
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)){ 
    Serial.println(F("Fallo OLED"));
    for(;;);
  }
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(10, 20);
  display.print(F("LISTO..."));
  display.display();
}

void loop(){
  float red, green, blue;
  tcs.getRGB(&red, &green, &blue);
  int r = (int)red;
  int g = (int)green;
  int b = (int)blue;

  Serial.print(r);
  Serial.print(",");
  Serial.print(g);
  Serial.print(",");
  Serial.println(b);
  //Escuchamos a python con 'M','L' o 'N'
  if(Serial.available() > 0){
    char orden = Serial.read();
    if (orden == 'M'){ 
      setColor(255, 0, 0); 
      mostrarPantalla("MANZANA", r, g, b);
    }else if(orden == 'L'){ 
      setColor(0, 255, 0); 
      mostrarPantalla("LIMON", r, g, b);
    }else if(orden == 'P'){ 
      setColor(255, 255, 0); 
      mostrarPantalla("PLATANO", r, g, b);
    }else if(orden == 'Z'){ 
      setColor(255, 127, 38); 
      mostrarPantalla("ZANAHORIA", r, g, b);
    }else if(orden == 'C'){ 
      setColor(90, 0, 255); 
      mostrarPantalla("CEBOLLA", r, g, b);
    }else if(orden == 'N'){ 
      setColor(0, 0, 0); 
      mostrarPantalla("ESPERANDO", r, g, b);
    }
  }
  delay(100); 
}

void setColor(int r, int g, int b){
  analogWrite(redPin,   255 - r);
  analogWrite(greenPin, 255 - g);
  analogWrite(bluePin,  255 - b);
}

void mostrarPantalla(String texto, int r, int g, int b){
  display.clearDisplay();
  
  display.setTextSize(2);
  display.setCursor(10, 10);
  display.println(texto);
  
  display.setTextSize(1);
  display.setCursor(0, 45);
  display.print("R:"); display.print(r);
  display.print(" G:"); display.print(g);
  display.print(" B:"); display.print(b);
  
  display.display();
}