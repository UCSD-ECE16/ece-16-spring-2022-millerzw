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

if __name__ == "__main__":
    fs = 50  # sampling rate
    num_samples = 250  # 5 seconds of data @ 50Hz
    process_time = 1  # compute the step count every second

    ped = Pedometer(num_samples, fs, [])
    ped.adjust_thresholds(12,40)
    # thresholds for walking with bluetooth is 15 30

    comms = Communication("COM4", 115200)
    comms.clear()  # just in case any junk is in the pipes
    comms.send_message("wearable")  # begin sending data
    sendSteps=0

    try:
        previous_time = time()
        while (True):
            message = comms.receive_message()
            if (message != None):
                try:
                    (m1, m2, m3, m4) = message.split(',')
                except ValueError:  # if corrupted data, skip the sample
                    continue

                # Collect data in the pedometer
                ped.add(int(m2), int(m3), int(m4))

                # if enough time has elapsed, process the data and plot it
                current_time = time()
                if (current_time - previous_time > process_time):
                    previous_time = current_time

                    steps, peaks, filtered = ped.process()
                    print("Step count: {:d}".format(steps))

                    sendSteps=steps

                    #comms.send_message(str(steps))
                    # plt.cla()
                    # plt.plot(filtered)
                    # plt.title("Step Count: %d" % steps)
                    # plt.show(block=False)
                    # plt.pause(0.001)
                # we want to always send the step number, not just on the 1 second time
                comms.send_message(str(sendSteps))


    except(Exception, KeyboardInterrupt) as e:
        print(e)  # Exiting the program due to exception
    finally:
        print("Closing connection.")
        comms.send_message("sleep")  # stop sending data
        comms.close()

