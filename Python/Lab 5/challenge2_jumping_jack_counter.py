from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.Pedometer import Pedometer
from matplotlib import pyplot as plt
from time import time

import numpy as np

if __name__ == "__main__":
    fs = 50  # sampling rate: this doesnt matter for this instance
    num_samples = 512  # 512 samples from arduino
    #process_time = 1  # compute the step count every second

    ped = Pedometer(num_samples, fs, [])
    ped.adjust_thresholds(12,40)

    jum = Pedometer(num_samples, fs, [])
    jum.adjust_thresholds(30,70)

    comms = Communication("COM4", 115200)
    comms.clear()  # just in case any junk is in the pipes
    comms.send_message("wearable")  # begin sending data
    sendSteps=0
    sendJumps=0

    steps=0
    jumps=0
    try:
        previous_time = time()
        while (True):
            message = comms.receive_message()
            if (message != None):
                try:
                    (m1, m2, m3, m4) = message.split(',')
                    print(message)
                except ValueError:  # if corrupted data, skip the sample
                    continue

                # Collect data in the pedometer
                ped.add(int(m2), int(m3), int(m4))
                jum.add(int(m2), int(m3), int(m4))

                # if enough time has elapsed, process the data and plot it
                current_time = time()
                #if (current_time - previous_time > process_time):
                if (int(m1)==511):
                    previous_time = current_time

                    steps, peaks, filtered = ped.process()
                    #steps=steps+1
                    print("Step count: {:d}".format(steps))

                    jumps, peaksJ, filteredJ = jum.process()
                    #jumps=jumps+1
                    print("Jump count: {:d}".format(jumps))

                    sendSteps=steps
                    sendJumps=jumps

                    #comms.send_message(str(steps))
                    plt.cla()
                    plt.plot(filtered)
                    plt.title("Step Count: %d" % steps)
                    plt.show(block=False)
                    plt.pause(0.001)
                # we want to always send the step number, not just on the 1 second time
                comms.send_message("steps " + str(sendSteps) + ",jumps " + str(sendJumps))
                #print("steps " + str(sendSteps) + ",jumps " + str(sendJumps))


    except(Exception, KeyboardInterrupt) as e:
        print(e)  # Exiting the program due to exception
    finally:
        print("Closing connection.")
        comms.send_message("sleep")  # stop sending data
        comms.close()

