## Zach Miller and Justin Kane Starr - Final Project
### A16568617 and A15554881

# ECE 16 Grand Challenge

## Space Invaders Controller

A socket-based controller for Space Invaders to controller the game wirelessly with the ESP32.

The game is a modified version of Space Invaders based off of this project: https://github.com/leerob/Space_Invaders

You must have Pygame installed before being able to run the game: https://www.pygame.org/

### Summary

In our final project we are required to finish two assignments. 
The first is make three improvements and add three features to
a supplied game of space invaders. These improvements and features are listed below.
Attached, there will also be a GIF of the game in action. Unfortunately, the bluetooth on my computer
was not working, so we could not show proof of either of the assignments running over bluetooth. My partner's
computer unfortunately does not have bluetooth.

###Requirements

__**Improvements**__: 
- Decouple fire and move by using the ppg as a fire button: This was done by sending an extra CSV to the python controller program
from the Arduino. At this stage it was "movement type","fire boolean".
- Smoother movement 
  - created thresholds for what angle is considered a movement. ie creating a dead space. 
- Random sprite movements.
  - The sprite group take their base velocity of 10 and added it with a list of 0, 10, 20 or 30

__**Features**__:
- Sensitivity setting
    -(hitting the button on the arduino switches the sensitivity between 3 options by changing the sampling frequency of the controller):
Once again this was done by sending an extra CSV to the python controller program from the Arduino. It ended up sending
3 value, a movement type, fire boolean, and 0-3 movement speed setting. In python there was an array containing
the three movement speed options that would be picked based on this value
- Display Score/Lives.
  - this was difficult because of socket overloading with too much data. We used a file to store the data instead and read from it using the controller: Note to run this on a different
machine, one would have to rename the file directory correctly.
- Motor Buzz when hit
  - The game would check if the last run through of the program had the same lives as the current using the string from the file we created, if they didn't match the motor would buzz.

### GIF
##### Note if images are broken on this page check submission by Justin Kane-Starr
![](images/Space_Invader.gif)

## Morse Code Translator

### Summary
The morse code translator takes inputs from the arduino which are read as
dits, dats and spaces, which are short,long presses of the button and long time between presses respectively, then sends them
to the computer in python. Python then uses a Dictionary that can translate the dit and dat pairs
using in-built python libraries. The read string is parsed between each space read from the arduino and translates
this sequence of dits and dats directly. Once there has been a long enough pause it will 
print out the word to the python terminal. In the GIF below we print out the statement "Hi Ramsin."

On the arduino side of things, we first created a system to differentiate dits and dashes by checking if
the length of the button being held was less than (dit) or longer than (dash) a constant variable denoted
at the top of the program. In this way the program can be tuned for the user if they are bad at morse code (as we both were).
Then we needed to create a differentiation between letters and words. We did this by making another timer to
where if the button hadn't been pressed down by a constant time as denoted at the top of the file, we would send
a denoter for letter. Then we would check if the last sent message was a letter denoter and even more time 
had passed since an input we would send a word denoter. We made sure to make booleans to check that there must
be some dits and dashes before we can consider a letter happening and there must be a letter before a space.

Then in python we were able to switch the messages from arduino to their more proper characters. Letters would
get spaces between them and words an extra space. Dits and dashes were kept as periods and hyphens. After,
it was a simple as using the dict and creating a "decoder" function that would turn the sentence to english.
We would save this sentence and periodically (when a new word was added) send it back to Arduino to show
up on the display.

### GIF
##### Note if images are broken on this page check submission by Justin Kane-Starr
![](images/Morse_Code.gif)