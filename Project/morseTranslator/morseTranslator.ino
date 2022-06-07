/*
 * Global variables
 */
// Acceleration values recorded from the readAccelSensor() function
int ax = 0; int ay = 0; int az = 0;
int ppg = 0;        // PPG from readPhotoSensor() (in Photodetector tab)
int sampleTime = 0; // Time of last sample (in Sampling tab)
bool sending;

const int BUTTON_PIN=13;  //Pin that button is on
int buttonState=0;    //
bool lastState=false;  //condition for button press


int startOfPress=0; //Start of Button Press time
int endOfPress=0;   //End of Button Press time
int heldPress=0;  //How long was button held
int letterWordTimer=0;  //Differentiate between letter or word

int currTime=0; //Time of currently

const int buzzTime = 250; //ms to s

String character="";
bool lastCommand=false; //check if the last command was a letter
bool allowSpace=false;  //check if the last command was a word

const int ditdotTimer=300; //differentiate between dit and dash, anything < = dit and > = dot

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
  pinMode(BUTTON_PIN, INPUT);
  sending = false;

  //Serial.begin(9600);
}

/*
 * The main processing loop
 */
void loop() {
  
  String command = receiveMessage();
  if(command == "stop") {
    sending = false;
    writeDisplay("Translator: Off", 0, true);
  }
  else if(command == "start") {
    sending = true;
    writeDisplay("Translator: On", 0, true);
  }
  else{
    sending=true;
    writeDisplay(command.c_str(),1, true);
    //writeDisplay("Translating", 0, true);
  }
  
  currTime=millis();
  // Send the dit or dash
  
  buttonState= digitalRead(BUTTON_PIN);
  //Serial.println(buttonState);
  if (buttonState==LOW && lastState==false){
    lastState=true;
    startOfPress=currTime;
  }
  if (lastState==true && buttonState==HIGH){//Button Released
    lastState=false;
    endOfPress=currTime;
  }
  //Serial.print("end of press: ");
  //Serial.print(endOfPress);
  //Serial.print("start of press: ");
  //Serial.print(startOfPress);
  //Serial.print(" ");
  
  heldPress=endOfPress-startOfPress;
  //Serial.println(heldPress);
  if (heldPress<ditdotTimer && heldPress>10){
    //Serial.println("DIT");
    sendMessage(".");
    startOfPress=endOfPress;
    lastCommand=true;
  }
  else if(heldPress>=ditdotTimer){
    //Serial.println("DOT");
    sendMessage("-");
    startOfPress=endOfPress;
    lastCommand=true;
  }
  //startOfPress=endOfPress; //putting this here after both would be better, however arduino is a bad program doing it this way breaks everything
  letterWordTimer= currTime-endOfPress;
  if (letterWordTimer >= 1000 && letterWordTimer < 2000 && lastCommand ==true){
    //Serial.println("Letter");
    sendMessage("l");
    lastCommand=false;
    allowSpace=true;
  }
  else if (letterWordTimer>= 2300 && allowSpace==true){
    //Serial.println("Space");
    sendMessage("w");
    allowSpace=false;
  }
  //if between 1500 and 2500 is a letter 
  //if between 2500 up is a word finish

  
}
