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
- Decouple fire and move by using the ppg as a fire button.
- Smoother movement 
  - created thresholds for what angle is considered a movement. ie creating a dead space. 
- Random sprite movements.
  - The sprite group take their base velocity of 10 and added it with a list of 0, 10, 20 or 30

__**Features**__:
- Sensitivity setting
    -(hitting the button on the arduino switches the sensitivity between 3 options by changing the sampling frequency of the controller). 
- Display Score/Lives
  - this was difficult because of socket overloading with too much data. We used a file to store the data instead and read from it using the controller. 
- Motor Buzz when hit
  - The game would check if the last run through of the program had the same lives as the current using the string from the file we created, if they didn't match the motor would buzz

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

### GIF
##### Note if images are broken on this page check submission by Justin Kane-Starr
![](images/Morse_Code.gif)