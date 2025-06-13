#include <Servo.h>
Servo myServo;


// Define pins
const int irSensor = 3;
const int motorIN3 = 13;
const int servoPin = 2;

const int lowerRoller = 40;
const int upperRoller = 150;

const unsigned long timeoutDuration = 3000;  // 3 seconds timeout

bool stop = false;
bool mode2_active = false;
String command = "";


void setup() {
  pinMode(irSensor, INPUT);
  pinMode(motorIN3, OUTPUT);

  Serial.begin(9600);
  myServo.attach(servoPin);  // Attach once and keep it attached

  delay(500);
}


void loop() {
  // Read serial command
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    command.trim();
    if (command == "s") {
      stopEverything();  // Interrupt any mode immediately
      return;
    }
  }

  // MODE 1: Run once and stop
  if (command == "mode1" && !mode2_active) {
    stop = false;
    Serial.println("MODE 1 ACTIVATE!");
    command = "";
    runFeedCycle(); // Run once
  }

  // MODE 2: Start continuous
  if (command == "mode2" && !mode2_active) {
    Serial.println("MODE 2 ACTIVATE!");
    mode2_active = true;
    stop = false;
    command = "";
  }

  // If in mode 2, keep running feed cycle
  if (mode2_active && !stop) {
    runFeedCycle();
  }
}


void runFeedCycle() {
  if (stop) return;

  Serial.println("Starting motor...");
  digitalWrite(motorIN3, HIGH);  // Start motor
  myServo.write(lowerRoller);    // Drop roller
  delay(300);

  Serial.println("Waiting for object...");
  unsigned long startTime = millis();
  while (digitalRead(irSensor) == HIGH) {
    if (checkStop() || stop) return;
    if (millis() - startTime >= timeoutDuration) {
      Serial.println("No object detected in time. Stopping...");
      stopEverything();
      return;
    }
  }

  Serial.println("Object detected!");
  myServo.write(upperRoller);    // Lift roller
  delay(100);

  while (digitalRead(irSensor) == LOW) {
    if (checkStop() || stop) return;
  }

  Serial.println("Object passed. Stopping motor.");
  digitalWrite(motorIN3, LOW);  // Stop motor
  myServo.write(lowerRoller);   // Drop roller again
  delay(1000); // delay for capturing images
  Serial.print("capture"); // signal the computer to capture
  delay(1300);  
}


bool checkStop() {
  if (Serial.available()) {
    String temp = Serial.readStringUntil('\n');
    temp.trim();
    if (temp == "s") {
      stopEverything();
      return true;
    }
  }
  return false;
}


void stopEverything() {
  Serial.println("Stopping everything.");
  digitalWrite(motorIN3, LOW);
  myServo.write(lowerRoller);
  stop = true;
  mode2_active = false;
  command = "";
}

