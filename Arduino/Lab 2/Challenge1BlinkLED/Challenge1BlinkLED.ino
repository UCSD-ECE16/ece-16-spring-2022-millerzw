const int LedA = 13;//led One
const int LedB = 12;//led Two
const int LedC = 27;//led Three

//blink a at 1 hz = 1 on 1 off   red
//blink b at 10 hz = .1 on .1 off   blue
//blink c at 50 hz = .02 on .02 off   yellow

int stateA=LOW;
int stateB=LOW;
int stateC=LOW;

//const long periodA = 1000;  // 1 s on and off
//const long periodB = 100;   // .1 s on and off
//const long periodC = 20;    // .02s on and off

int periodA;
int periodB;
int periodC;

const long redOn=1000;    //1 s on
const long redOff=100;    // 100ms off

const long blueOn=200;    //1 s on
const long blueOff=50;    // 100ms off

const long yellowOn=20;    //1 s on
const long yellowOff=10;    // 100ms off

unsigned long prevTimeA=millis();
unsigned long prevTimeB=millis();
unsigned long prevTimeC=millis();


void setup() {
  // put your setup code here, to run once:
  pinMode(LedA,OUTPUT);
  pinMode(LedB,OUTPUT);
  pinMode(LedC,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long nowTime=millis();
  
  if (nowTime-prevTimeA>=periodA){// if the elapsed time has passed
    prevTimeA=millis();
    if (stateA==LOW){
      stateA=HIGH;
      periodA=redOn;//set to red on timer
    }else{
      stateA=LOW;
      periodA=redOff;//set to red off timer
    }
    digitalWrite(LedA,stateA);
  }
  if (nowTime-prevTimeB>=periodB){// if the elapsed time has passed
    prevTimeB=millis();
    if (stateB==LOW){
      stateB=HIGH;
       periodB=blueOn;//set to blue on timer
    }else{
      stateB=LOW;
      periodB=blueOff;//set to blue off timer
    }
    digitalWrite(LedB,stateB);
  }
  if (nowTime-prevTimeC>=periodC){// if the elapsed time has passed
    prevTimeC=millis();
    if (stateC==LOW){
      stateC=HIGH;
      periodC=yellowOn;//set to yellow on timer
    }else{
      stateC=LOW;
      periodC=yellowOff;//set to yellow off timer
    }
    digitalWrite(LedC,stateC);
  }
  Serial.print("A: ");
  Serial.print(stateA);
  Serial.print(" B: ");
  Serial.print(stateA);
  Serial.print(" C: ");
  Serial.print(stateA);
  Serial.println("");
  

}
