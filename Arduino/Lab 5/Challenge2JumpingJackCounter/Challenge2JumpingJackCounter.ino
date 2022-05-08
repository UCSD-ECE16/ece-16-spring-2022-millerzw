int sampleTime = 0; // Time of last sample (in Sampling tab)
int ax = 0; int ay = 0; int az = 0; // Acceleration (from readAccelSensor())
bool sending;

int axArray[512];
int ayArray[512];
int azArray[512];

int i=0;
int j=0;

const int BUTTON_PIN=13;
bool conA=false;

void setup() {
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  sending = false;
  writeDisplay("Sleep", 0, true);
  Serial.begin(115200);
}

void loop() {
  String command = receiveMessage();
  if(command == "sleep") {
    sending = false;
    writeDisplay("Sleep", 0, true);
  }
  else if(command == "wearable") {
    sending = true;
    writeDisplay("Wearable", 0, true);
  }
  else{
    sending=true;
    //recieving input in form steps #,jumps #
    writeDisplayCSV(command.c_str(),1);
  }
  if(sending && sampleSensors()) {
    //String response = String(sampleTime) + ",";
    //response += String(ax) + "," + String(ay) + "," + String(az);
    //sendMessage(response);
    i=i%512;
    if (i<512){
      axArray[i]=ax;
      ayArray[i]=ay;
      azArray[i]=az;
      i++;
    }
  }
  if (digitalRead(BUTTON_PIN)==LOW){//Button down
    conA=true;
  }
  if (conA==true && (digitalRead(BUTTON_PIN)==HIGH)){//button released
    conA=false;
    //send arrays to arduino
    //Serial.println("BUTTON");
    if (sending){
      for (j=0;j<512;j++){
        String response = String(j) + ",";
        response += String(axArray[j]) + "," + String(ayArray[j]) + "," + String(azArray[j]);
        sendMessage(response);
        //axArray[j]=0;
        //ayArray[j]=0;
        //azArray[j]=0;
      }
    }
    i=0;//reset i
  }
}
