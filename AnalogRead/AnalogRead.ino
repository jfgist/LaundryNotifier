/*
September 22, 2014 

Read value(s) from a vibration sensor and pass those out through some interface.
(Maybe SPI, I2C or Serial/USB)
*/

int sensorPin1 = 0;    // input pin for sensor 1
int sensorPin2 = 1;    // input pin for sensor 2
int sensorPin3 = 2;    // input pin for sensor 3
int sensorPin4 = 3;    // input pin for sensor 4

int ledPin = 13;      // LED pin
int sensorValue1 = 0;  // variable to store the value coming from the sensor
int sensorValue2 = 0;  // variable to store the value coming from the sensor
int sensorValue3 = 0;  // variable to store the value coming from the sensor
int sensorValue4 = 0;  // variable to store the value coming from the sensor

void setup() {
  Serial.begin(9600);         // open serial connection
  pinMode(ledPin, OUTPUT);    // declare the ledPin as an OUTPUT:
}

void loop() {
  // read the value from the sensor:
  sensorValue1 = analogRead(sensorPin1);    
  sensorValue2 = analogRead(sensorPin2);    
  sensorValue3 = analogRead(sensorPin3);
  sensorValue4 = analogRead(sensorPin4);
  
  if (Serial.available())
  {
    switch(Serial.read()) {
      case 'Sensor1':
         Serial.write(sensorValue1);
         break;
      case 'Sensor2':
         Serial.write(sensorValue2);
         break;
      case 'Sensor3':
         Serial.write(sensorValue3);
         break;
      case 'Sensor4':
         Serial.write(sensorValue4);
         break;
    }
    delay(100); //might not need this.  Probably need delay on the pi side
    //  Serial.print("X Sensor Value: ");
    //  Serial.print(sensorValue1);
    //  Serial.print("\tY Sensor Value: ");
    //  Serial.print(sensorValue2);
    //  Serial.print("\tZ Sensor Value: ");
    //  Serial.println(sensorValue3);
    //  delay(100);
    // turn the ledPin on
    // digitalWrite(ledPin, HIGH);  
  }
}
