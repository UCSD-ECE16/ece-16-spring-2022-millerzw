const int BUTTON_PIN = 13; //map button to pin 13

int timer=0; //time left

unsigned long prevTime=millis();
unsigned long prevTimeB=millis();
unsigned long prevTimeC=millis();

int threeSecond=3000; //3s=3000ms
int oneSecond=1000; //1s=1000ms
int hundredMillis=100; //100ms

bool conA=false;

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  //low=0 is pressed down
  //high=1 is released
  
  if (digitalRead(BUTTON_PIN)==LOW){ //button pressed down
    conA=true;
    //Serial.print("A");
  }
  if (conA==true && digitalRead(BUTTON_PIN)==HIGH){ //button released
    timer+=1; //add 1 to timer and reset condition a
    conA=false;
    prevTime=millis();
    //Serial.print("B");
  }

  
  unsigned long nowTime=millis(); 
  if (nowTime-prevTime>=threeSecond){//if 3 seconds passed since last press
    if (nowTime-prevTimeB>=oneSecond){//decrement 1 every second
      prevTimeB=millis();
      timer-=1;
    }
  }
  if (timer<=-1){ //make sure it doesnt drop below 0
    timer+=1;
  }
  if (nowTime-prevTimeC>=hundredMillis){//display every 100ms
    prevTimeC=millis();
    Serial.println(timer);
  }
  
  
  
  

}
