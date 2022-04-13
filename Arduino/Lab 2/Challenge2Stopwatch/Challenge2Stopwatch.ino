const int BUTTON_PIN = 13; //map button to pin 13

int counter=0;

unsigned long prevTime=millis();
unsigned long prevTimeB=millis();

int oneSecond=1000; //1s=1000ms
int hundredMillis=100; //100ms

bool playing=false;

bool conA=false;
bool conB=false;

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (playing==false){
    if (digitalRead(BUTTON_PIN)==LOW){ //button pressed down
      conA=true;
    }
    if (conA==true && digitalRead(BUTTON_PIN)==HIGH){ //button released
      playing=true;
    }
  }
  else if(playing==true){
    if (digitalRead(BUTTON_PIN)==LOW){ //button pressed down
      conA=false;
    }
    if (conA==false && digitalRead(BUTTON_PIN)==HIGH){ //button released
      playing=false;
    }
  }
  unsigned long nowTime=millis();
  if (playing){
    
    if (nowTime-prevTime>=oneSecond){
      prevTime=millis();
      counter+=1;
    }
  }
  if (nowTime-prevTimeB>=hundredMillis){
    prevTimeB=millis();
    Serial.println(counter);
  }
  
  
  

}
