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
    This challenge is closely mirrored by the tutorial 2 code. It just
    requires us to keep track of the milliseconds between when the lights
    should be on and off. We can check if the current time is greater than
    the alotted period for each light and if so, change the state of the light.
    Doing it this way prevents the code from stopping at each delay and
    messing up the periods of other light cycles.
    ![](images/challenge1A.gif)
    ![](images/challenge1B.gif)

---
**Challenge_2** :
    This challenge relied on understanding how we can use millis as a counter
    as well as how we can determine when a button is pressed. To check for
    a button press we need to make sure the last state of the button was 
    down=0 or low and the current state is up=1 or high. Once the button is 
    pressed we switch between two states, either playing the counter or not
    playing the counter. This was accomplished through a boolean. When playing
    we would run a millis() check for every second we would increment the
    stopwatch. A seperate millis() comparator was used to display the output
    on a unique clock cycle.
    
![](images/Challnege2.gif)
---
**Challenge_3** :
    In some essence, this was a modified version of challenge 2, where instead
    of a playing condition we have a countdown condition. If the button
    is pressed by the same check in the previous challenge we need to record
    at what time it was last pressed and increment a counter by one. We then
    use a millis check and see if the current time is within 3 seconds of the
    last button press. If not then we create a 1s delay between decrementing
    the counter until 0 or until the button is pressed again.
    ![](images/Challenge3.gif)


---