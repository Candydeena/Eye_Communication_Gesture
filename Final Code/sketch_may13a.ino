#include <Servo.h>

int motorPin1 = 5;
int motorPin2 = 6;
int servoPin = 9;
Servo myServo;  // Create a Servo object to control the servo motor

void setup() {
  Serial.begin(9600);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  myServo.attach(servoPin);  // Attach the servo motor to the pin
}

void loop() {
  if (Serial.available()) {
    int command = Serial.parseInt();
    
    if (command == 1) {  // RIGHT
      // Rotate servo to a specific angle for "RIGHT"
      myServo.write(10);  // Rotate servo to 90 degrees (example for right)
    } else if (command == 2) {  // LEFT
      // Rotate servo to a specific angle for "LEFT"
      myServo.write(170);  // Rotate servo to 0 degrees (example for left)
    }
     else if (command == 3) {  // FORWARD
      // Control motors for forward movement
      digitalWrite(motorPin1, HIGH);
     digitalWrite(motorPin2, LOW);
    } else if (command == 4) {  // BACKWARD
      // Control motors for backward movement
      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, HIGH);
    } else if (command == 5) {  // STOP
      // Stop the motors and set servo to neutral position
      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, LOW);
      myServo.write(90);  // Set servo to neutral position (e.g., 90 degrees)
    }
  }
}
