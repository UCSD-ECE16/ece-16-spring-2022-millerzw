int sampleTime = 0; // Time of last sample (in Sampling tab)
int ax = 0; int ay = 0; int az = 0; // Acceleration (from readAccelSensor())
bool sending;

unsigned long currTime=0;
unsigned long startOfBuzz=0;

bool toggle=false;

const int oneSec=1000;//1000ms = 1 s

void setup() {
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  setupMotor();
  sending = false;
  writeDisplay("Sleep", 0, true);
}

void loop() {
  currTime=millis();
  String command = receiveMessage();
  if(command == "sleep") {
    sending = false;
    writeDisplay("Sleep", 0, true);
  }
  else if(command == "wearable") {
    sending = true;
    writeDisplay("Wearable", 0, true);
  }
  else if(command == "inactive"){
    sending=true;
    writeDisplay("Inactive",0, true);
    //Buzz motor for 1 second
    
    if (!toggle){
      toggle=true;
      startOfBuzz=millis();
    }
    
  }
  else if(command == "active"){
    sending=true;
    writeDisplay("Active",0,true);
  }
  if(sending && sampleSensors()) {
    String response = String(sampleTime) + ",";
    response += String(ax) + "," + String(ay) + "," + String(az);
    sendMessage(response);    
  }
  
  if (currTime-startOfBuzz<=oneSec){
    activateMotor(200);
  }
  else{
    toggle=false;
    deactivateMotor();
  }
  
}
