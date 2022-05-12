#### by: Zach Miller A16568617

##ReadMe

---
Started: 05/02/2022

---
---
**Tutorial 1** :

We can have multiple things on one 12c line because each device has its own address
and so despite the same wires we can separate how they receive the information.

The while(1) statement creates an infinite loop that stops anything from happening.

led Brightness of 25mA ledBrightness= 122.5. Red+Ir ledMode=2. sampleRate=200. adcRange
=8192.

It changes the amount of time the LEDs shine into the finger before determining if
there was a pulse. A larger number = longer led on time for the leds. Units are microSeconds

14 bits are needed for 18384 adc

red w= 660nm, ir w= 880nm, green w= 537nm

To get green, use mode 3 and use particleSensor.getGreen()


---
---
**Tutorial 2** :



---
---
**Tutorial 3** :



---
---
**Challenge 1** :

I only changed the design of the HRMonitor slightly to achieve the beats wanted. I added
a lowpass filter to further try to smooth the signal and reduce noise. I found that
this got my correlation from about 0.82 to 0.99. I believe the issue with my HRM at
this stage is more to do with my counting of the heartbeats outside the scope of python.
It seemed as if for every signal I counted one at the start or end that wasn't captured
by python and thus my csv files were lacking them despite me counting them during the 
upload process.

---
---
**Challenge 2** :


---