#include "ESP8266WiFi.h"


const int BUTTON_PIN = 4;    // Define pin the button is connected to
const int ON_BOARD_LED = 2;  // Define pin the on-board LED is connected to
const int RGB_G_PIN = 12;    // RGB Green LED
const int LDR_PIN = A0;   
int s=0, avg=0;// Define the analog pin the LDR is connected to
//===============================================================================
//  Initialization
//===============================================================================
void setup() {
  pinMode(ON_BOARD_LED, OUTPUT);       // Initialize the LED_BUILTIN pin as an output
  pinMode(BUTTON_PIN, INPUT_PULLUP);  // Initialize button pin with built-in pullup.
  digitalWrite(ON_BOARD_LED, HIGH);    // Ensure LED is off
  Serial.begin(115200);               // Set comm rate to 115200
  
  Serial.println("Setup done");
}
//===============================================================================
//  Main
//===============================================================================
void loop() {
  int btn_Status = HIGH;
  int lightIntensity;
  if (s == 0){
    avg = 0;
    for (int i = 0; i < 10; i++){
      lightIntensity = analogRead(LDR_PIN);  // Read the light intensity
      analogWrite( RGB_G_PIN, map(lightIntensity, 40, 1023, 0, 1023));
//      Serial.printf("cur int - %d\n", lightIntensity);
      avg += lightIntensity;
//      Serial.printf("cur sum - %d\n", avg);
    }
    avg /= 10;
//    Serial.printf("avg - %d", avg);
//    Serial.println("");
//    Serial.println("");

  }
    lightIntensity = analogRead(LDR_PIN);  // Read the light intensity
    analogWrite( RGB_G_PIN, map(lightIntensity, 40, 1023, 0, 1023));

    s++;
    if (s == 1000){
      s=0;
      }
//    Serial.print("Light Intensity Reading: ");
    Serial.println(lightIntensity);
//    Serial.println("scan start");
    digitalWrite(ON_BOARD_LED, LOW);       // Turn LED ON
 
    digitalWrite(ON_BOARD_LED, HIGH);    // Turn LED Off
    btn_Status = digitalRead (BUTTON_PIN);  // Check status of button
    if (btn_Status == LOW) {
      delay(1000000);
    }   
  }
