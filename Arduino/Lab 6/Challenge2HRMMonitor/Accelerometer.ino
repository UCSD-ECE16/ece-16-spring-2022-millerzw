const int accelX=A2;
const int accelY=A3;
const int accelZ=A4;

//Set accelerometer pins as input
void setupAccelSensor(){
  pinMode(accelX,INPUT);
  pinMode(accelY,INPUT);
  pinMode(accelZ,INPUT);
}
//Read the pins
void readAccelSensor(){
  ax=analogRead(accelX);
  ay=analogRead(accelY);
  az=analogRead(accelZ);
}
