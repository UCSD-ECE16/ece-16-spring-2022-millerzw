const int BUTTON_PIN=13; //map button to pin 13

int oneSecond=1000; //1s = 1000ms
int twoSecond=2000; //2s = 2000ms

int buttonCurr=0;
int buttonPrev=0;
int startOfPress=0;
int endOfPress=0;


const int threshold=80; // threshold for whats considered a tap
const int timeBetween=200;  //time between tap checks to stop one tap counting for multiple

int sampleTime=0;//time of last sample

int ax=0;//current x of accelerometer
int ay=0;//current y of accelerometer
int az=0;//current z of acceletometer

int totalX=0;//average of all X samples
int totalY=0;//avergage of all Y samples
int totalZ=0;//avergae of all Z samples

int avgX=0;//average of all X samples
int avgY=0;//avergage of all Y samples
int avgZ=0;//avergae of all Z samples

int numTaps=0;  //number of taps
int sampleCount=0;  //number of samples taken

int currMillis=millis();  //current time
int lastMillis=millis();  //previous time

int lastTap=millis();     //last time of a tap
int prevTimeTimer=millis(); //last time the mini 1 second timer went off

void setup() {
  // put your setup code here, to run once:
  setupAccelSensor();
  setupDisplay();
  setupMotor();
  pinMode(BUTTON_PIN,INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

  //-------------
  //BUTTON LOGIC + Reset Case:
  
  //Check to see how long button is held down
  buttonCurr=digitalRead(BUTTON_PIN);
  if (buttonCurr==LOW){
    if (buttonPrev==HIGH){
      //start of press
      startOfPress=millis();
    }
    else if (buttonPrev==LOW){
      //still pressed down
      endOfPress=millis();
    }
  }else{
    startOfPress=0;
    endOfPress=0;
  }
  buttonPrev=buttonCurr;
  if (endOfPress>=startOfPress+twoSecond){
    numTaps=0;
  }
  
  //-------------
  //Checking Taps + updating last tap timer
  
  if (sampleSensors() && Serial.availableForWrite()){
      sampleCount++;
      totalX+=ax;
      totalY+=ay;
      totalZ+=az;
  
      avgX=totalX/sampleCount;
      avgY=totalY/sampleCount;
      avgZ=totalZ/sampleCount;
      currMillis=millis();
    //needs to be on a clock cycle to prevent multiple from 1 tap
    if ((ax>=threshold+avgX || az>=threshold+avgZ || az>=threshold+avgZ) && currMillis>=lastMillis+200){
      numTaps++;
      lastMillis=currMillis;
      lastTap=currMillis;
      
    }
    char str[8];
    itoa(numTaps,str,10);
    writeDisplay(str,0,true);
    /*
    Serial.print(ax);
    Serial.print(",");
    Serial.print(ay);
    Serial.print(",");
    Serial.println(az);
    */
  }
  //-------------
  //Check Time Between Taps + Update
  if (currMillis-lastTap>=(2*twoSecond)){
    if (currMillis-prevTimeTimer>=oneSecond){
      prevTimeTimer=millis();
      numTaps--;
    }
  }
  if (numTaps<=-1){
    numTaps=0;
  }

  //-------------
  //Buzz Motor Case
  if (numTaps==0){
    activateMotor(255);
  }else{
    deactivateMotor();
  }
  
  //-------------
  

}
