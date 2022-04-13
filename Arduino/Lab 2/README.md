#### by: Zach Miller A16568617

##ReadMe

---
Started: 4/11/2022

---
---
**Tutorial 1** :
    Install Arduino IDE from their website along with the esp32 package from
    the github repo provided in the tutorial documentation. This will allow
    you to use your esp32 microcontroller with Arduino

---
**Tutorial 2** :
    This will show how we can use Digital Write and Read for buttons and LEDS
    with our microcontroller and Arduino. Specifically its important to see
    how we can use the millis of the computer instead of a delay to prevent
    code our code from stopping completely as something executes.

---
**Tutorial 3** :
    Firstly, we can see how we are able to print to serial in order to put
    any messages on the screen, and also check to make sure that the data 
    we are reading in from our sensors is correct.

---
**Challenge_1** :
    This challenge is closely mirroeed by the tutorial 2 code. It just
    requires us to keep track of the milliseconds between when the lights
    should be on and off. We can check if the current time is greater than
    the alotted period for each light and if so, change the state of the light.
    Doing it this way prevents the code from stopping at each delay and
    messing up the periods of other light cycles.

---
**Challenge_2** :
    

---
**Challenge_3** :
    


---