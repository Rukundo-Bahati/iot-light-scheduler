#include <Arduino.h>

const int relayPin = 2;  // Change this to your actual relay pin

void setup() {
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH); // Start with relay OFF (assuming active-low)
  Serial.println("Arduino ready");
}

void loop() {
  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    
    if (cmd == "1") {
      digitalWrite(relayPin, LOW); // Relay ON
      Serial.println("Light ON");
    } 
    else if (cmd == "0") {
      digitalWrite(relayPin, HIGH); // Relay OFF
      Serial.println("Light OFF");
    }
    else {
      Serial.print("Unknown command: ");
      Serial.println(cmd);
    }
  }
}