from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.Pedometer import Pedometer
from matplotlib import pyplot as plt
from time import time


# def load_data(filename):
#     return np.genfromtxt(filename, delimiter=",")
#
#
# # Load the data as a 500x4 ndarray
# data = load_data("./data/accelerometer.csv")
# t = data[:, 0]
# t = (t - t[0]) / 1e3
# ax = data[:, 1]
# ay = data[:, 2]
# az = data[:, 3]
#
# # Test the Pedometer with offline data
# ped = Pedometer(500, 50, [])
# ped.adjust_thresholds(12,40)
# ped.add(ax, ay, az)
# steps, peaks, filtered = ped.process()
#
# # Plot the results
# plt.plot(t, filtered)
# plt.title("Detected Peaks = %d" % steps)
# plt.plot(t[peaks], filtered[peaks], 'rx')
# plt.plot(t, [ped.get_low()] * len(filtered), "b--")
# plt.plot(t, [ped.get_high()] * len(filtered), "b--")
# plt.show()

###################################

import numpy as np
MORSE_DICT = { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----'}

def morseToEng(word):

    result=""
    spaceLoc=""
    i=0
    print("here")

    for letter in word:
        if (letter != " "):
            i=0

            spaceLoc+= letter
        else:
            i =i+1
            if (i==2):
                result+=" "
            else:
                result+=list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(spaceLoc)]
                spaceLoc=""
    return  result

print(morseToEng(".... ..  .... --- .--  "))
#m1              ".... ..   ....   --- .- -   "
#m2              ".... ..  .... --- .--  "

if __name__ == "__main__":
    fs = 50  # sampling rate
    num_samples = 250  # 5 seconds of data @ 50Hz
    process_time = 1  # compute the step count every second



    comms = Communication("COM4", 115200)
    comms.clear()  # just in case any junk is in the pipes
    comms.send_message("start")  # begin sending data

    word=""
    letter=""

    try:
        previous_time = time()
        while (True):
            message = comms.receive_message()
            if (message != None):
                try:
                    currChar= message[0]
                    print(currChar)
                except ValueError:  # if corrupted data, skip the sample
                    continue
                if (currChar=="."):
                    #we havea dit
                    word+=currChar
                elif (currChar=="-"):
                    #we have a dash
                    word+=currChar
                elif (currChar=="l"):
                    #end of the letter
                    word+=" "
                elif (currChar=="w"):
                    #end of the word
                    word+=" "
                    print(word)

                # Collect data in the pedometer
                #word=word+currChar

                # if enough time has elapsed, process the data and plot it
                current_time = time()
                if (current_time - previous_time > process_time):
                    previous_time = current_time

                    #send word to arduino
                # we want to always send the step number, not just on the 1 second time
                #comms.send_message(str(sendSteps))


    except(Exception, KeyboardInterrupt) as e:
        print(e)  # Exiting the program due to exception
    finally:
        print("Closing connection.")
        comms.send_message("sleep")  # stop sending data
        comms.close()

