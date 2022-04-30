
#### by: Zach Miller A16568617

##ReadMe

---
Started: 4/25/2022

---
---
**Tutorial 1** :

>Q1: the output is 
> 
><__main__.Dog object at 0x0000012B72DA7FD0>
> 
>Scout
> 
>2
> 
>The first is for the print of the object dog we created, the second is when we fetch
>its name from memory and the third its age from memory
> 
>Q2: 
> 
>Breed is encapsulated so we cant access it directly like the other without a helper 
>function
> 
>Q3: 
> 
>skippy = Dog("Skippy",4,"Rotweiler")
> 
>skippy.define_buddy(scout)
> 
>scout.buddy.description()

This tutorial showed the advantages of keeping function inside classes so our main
comes across much cleaner and readable

---
---
**Tutorial 2** :

This tutorial went over how we can use matplotlib with sampling to have python
display a graph of variables stored within arrays

---
---
**Tutorial 3** :

This tutorial went over how we can use a custom CircularList along with matplotlib
and sampling in order to create a live updating graph. THis is especially useful
to having data that comes from arduino be readable on the screen for analyzing
different factors and any possible errors.

---
---
**Challenge 1** :

This challenge just required us to do some basic transformations on our lists
such as taking the average over the period and the delta. I chose to make a 
custom operation of taking the distance between the last two values received from
Arduino. I don't think there were any roadbumps for this challenge as it mainly
required some basic understanding of how to do operations on Lists. The data
was very insightful as it showed the "faults" in the sensor, as in, even when still
it detected some movement. The transformation such as the average value was very
useful, and was very similar to how I approached a previous Lab when I was trying
to find if there was a tap. It also came in handy for the second challenge

![](images/challenge1gif.gif)

---
---
**Challenge 2** :

The average value was the key to detecting if someone was inactive or active here.
For checking inactivity, I would check the first and last average of the list, and
as long as they were within a threshold variable(1), then there had not been
significant movement during the period, and I would write Inactive to Arduino. I 
would also check for activity, as in the last sample was greater than the average +
some variable(60) or less than the average - that variable, then the person had
definitely moved, and I would write to Arduino Active.

![](images/challenge23gif.gif)

---
---
**Challenge 3** :

This Challenge was a matter of converting Challenge 2 into an OOP version. The
biggest struggle I ran into here was knowing whether to put the check for the
receiving of the main message within the class or within the main code. I learned
through trial and error it should be in main. I kept a few variables private such as
the baud rate, but within the scope of this assignment, I don't believe it changes
the outcome at all.

The Gif is the same as Challenge 2. See above

---


