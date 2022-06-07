/*
 * Global variables
 */
// Acceleration values recorded from the readAccelSensor() function
int ax = 0; int ay = 0; int az = 0;
int ppg = 0;        // PPG from readPhotoSensor() (in Photodetector tab)
int sampleTime = 0; // Time of last sample (in Sampling tab)
bool sending;

const int BUTTON_PIN=13;  //Pin that button is on
bool conA=false;  //condition for button press
int state=0;    //state of move speed

int motorTime=0; //Time of start of Motor Buzz for on hit
int currTime=0; //Time of currently

const int buzzTime = 250; //ms to s

/*
 * Initialize the various components of the wearable
 */
void setup() {
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  setupPhotoSensor();
  setupMotor();
  pinMode(LED_BUILTIN, OUTPUT);
  sending = false;

  writeDisplay("Ready...", 1, true);
  writeDisplay("Set...", 2, false);
  writeDisplay("Play!", 3, false);
  //Serial.begin(115200);
}

/*
 * The main processing loop
 */
void loop() {
  // Parse command coming from Python (either "stop" or "start")
  //readAccelSensor();
  //int b= getOrientation();
  //Serial.print("orientation: ");
  //Serial.println(String(b));
  //Serial.print("ax: "); Serial.print(ax);
  //Serial.print(" ay: "); Serial.print(ay);
  //Serial.print(" az: "); Serial.println(az);
  //readPhotoSensor();
  //Serial.println(String(getTaps()));
  
  String command = receiveMessage();
  if(command == "stop") {
    sending = false;
    writeDisplay("Controller: Off", 0, true);
  }
  else if(command == "start") {
    sending = true;
    writeDisplay("Controller: On", 0, true);
  }
  else if(command == "dead"){
    sending=true;
    motorTime=millis();
    //digitalWrite(LED_BUILTIN, HIGH);
  }
  else{
    sending=true;
    writeDisplayCSV(command.c_str(),1);
  }
  currTime=millis();

  // Send the orientation of the board
  if(sending && sampleSensors()) {
    String response = String(getOrientation()) + ",";
    response += String(state) + ",";
    response += String(getTaps());
    // Type of Move , Speed of move, Shooting or not Shooting
    sendMessage(response);
    
    //sendMessage(String(getOrientation()));
  }

  if (digitalRead(BUTTON_PIN)==LOW){//Button Down
    conA=true;
  }
  if (conA==true && digitalRead(BUTTON_PIN)==HIGH){//Button Released
    conA=false;
    state=state+1;
    state=state%3;
    //Switch between 3 states which are the spped of movement mode
  }

  if (currTime-motorTime <=buzzTime){
    activateMotor(200);
  }
  else{
    deactivateMotor();
  }
}
