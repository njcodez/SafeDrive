#include <Arduino.h>
#include "tensorflow_lite.h" 

void setup() {

  tfl.begin();
  camera.begin();
}

void loop() {
  camera.capture(image);
  float result = tfl.infer(image);
  if (result > THRESHOLD) {
    Serial.println("Driver is drowsy");
  } else {
    Serial.println("Driver is alert");
  }
  delay(1000);
}
