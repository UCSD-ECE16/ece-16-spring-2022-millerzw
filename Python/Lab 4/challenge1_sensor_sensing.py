from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from matplotlib import pyplot as plt
from time import time
import numpy as np

if __name__ == "__main__":
    num_samples = 100  # 2 seconds of data @ 50Hz
    refresh_time = 0.1  # update the plot every 0.1s (10 FPS)

    times = CircularList([], num_samples)  # Original 4 lists
    ax = CircularList([], num_samples)
    ay = CircularList([], num_samples)
    az = CircularList([], num_samples)

    average_x = CircularList([], num_samples)  # New 5 lists
    delta_x = CircularList([], num_samples)
    L1 = CircularList([], num_samples)
    L2 = CircularList([], num_samples)
    transformed = CircularList([], num_samples)

    comms = Communication("COM4", 115200)
    comms.clear()  # just in case any junk is in the pipes
    comms.send_message("wearable")  # begin sending data

    numberSamples = 1
    totalCount = 0

    try:
        previous_time = 0
        while (True):
            message = comms.receive_message()
            if (message != None):
                try:
                    (m1, m2, m3, m4) = message.split(',')
                except ValueError:  # if corrupted data, skip the sample
                    continue

                # add the new values to the circular lists
                times.add(int(m1))
                ax.add(int(m2))
                ay.add(int(m3))
                az.add(int(m4))

                # perform operations on the data
                # Average operation
                currAvg= sum(ax) / np.count_nonzero(ax)
                average_x.add(currAvg)

                # Sample Difference operation
                currDelta= abs(ax[-1] - ax[-2])
                delta_x.add(currDelta)

                # Euclidian Distance operation
                currL2= np.sqrt(np.square(ax[-1]) + np.square(ay[-1]) + np.square(az[-1]))
                L2.add(currL2)

                # Sum of absolutes
                currAbs= abs(ax[-1])+ abs(ay[-1])+ abs(az[-1])
                L1.add(currAbs)

                # Distance between last two values
                currDistance = np.sqrt(np.square(ax[-1]-ax[-2]) + np.square(ay[-1]-ay[-2])+ np.square(az[-1]-az[-2]))
                transformed.add(currDistance)

                # if enough time has elapsed, clear the axis, and plot az
                current_time = time()
                if (current_time - previous_time > refresh_time):
                    previous_time = current_time
                    plt.cla()
                    plt.plot(ax, label='ax', color='red')
                    plt.plot(ay, label='ay', color='blue')
                    plt.plot(az, label='az', color='green')

                    plt.plot(average_x, label='average_x', color='cyan')
                    plt.plot(delta_x, label='delta_x', color='magenta')
                    plt.plot(L2, label='L2', color='yellow')
                    plt.plot(L1, label='L1', color='black')
                    plt.plot(transformed, label='distance', color='grey')

                    plt.show(block=False)
                    plt.pause(0.001)
    except(Exception, KeyboardInterrupt) as e:
        print(e)  # Exiting the program due to exception
    finally:
        comms.send_message("sleep")  # stop sending data
        comms.close()
