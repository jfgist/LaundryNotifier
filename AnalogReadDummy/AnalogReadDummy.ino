/*
September 22, 2014 

Read value(s) from a vibration sensor and pass those out through some interface.
(Maybe SPI, I2C or Serial/USB)
*/

int sensorPin1 = 0;    // input pin for sensor 1
int sensorPin2 = 1;    // input pin for sensor 2
int sensorPin3 = 2;    // input pin for sensor 3
int sensorPin4 = 3;    // input pin for sensor 4

int incoming = 0;

int ledPin = 13;      // LED pin
int sensorValue1 = 1000;  // variable to store the value coming from the sensor
int sensorValue2 = 2000;  // variable to store the value coming from the sensor
int sensorValue3 = 3000;  // variable to store the value coming from the sensor
int sensorValue4 = 4000;  // variable to store the value coming from the sensor

void setup() {
  Serial.begin(9600);         // open serial connection
  pinMode(ledPin, OUTPUT);    // declare the ledPin as an OUTPUT:
}

void loop() {
  // read the value from the sensor:

  
  if (Serial.available())
  {
    incoming = Serial.read()-'0';
    
    if (incoming == 1){
      Serial.print(sensorValue1);
      sensorValue1 = sensorValue1 + 1;
    }
    
    Serial.print("Incoming received: ");
    Serial.println(incoming);
    Serial.write(incoming);
        
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
