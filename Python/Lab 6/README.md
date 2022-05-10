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



---
---
**Challenge 2** :

This challenge was very similar to Challenge1 but with some more work on the arduino
side of things. A jump counter is essentially a less sensitive step counter, so we
can re-use the pedometer but with a high min/max value check. It was important then
to create a function in the Pedometer class to update the min/max values to more
easily be able to tune both the steps and the jumps. As well as creating a function
to return the min and max values in order to not worry about the scale on the graph.
On arduino we are now
keeping a buffer of the last samples, and sending them to Python only when the button
is pressed. To accomplish this I filled an 512 size array by using the index i%512
which essentially loops through the array. We did a button check like we did in earlier
labs where a full press would be required to send the data over. So in python the code
is modified from challenge 1 to always be trying to receive data, which it will only
process once we get our buffer sent in and then display back both a jump and step
count. Again, for the video purpose I used my hand with motion, but got correctly tuned
min/max values from a csv file provided to me by a classmate which has been noted in 
the challenge 2 comment section.

![](images/gifVidTwo.gif)
---