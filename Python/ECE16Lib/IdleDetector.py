from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from matplotlib import pyplot as plt
from time import time
import numpy as np

class IdleDetector():
    com_name=""
    __baudrate=115200
    numSamples=250
    refreshTime=0.1
    __moveThresh=60
    __avgThresh=1


    average_x = CircularList([], numSamples)  # New 5 lists

    def __init__(self, com_name, baudrate):
        self.com_name=com_name
        self.__baudrate=baudrate

    def checkCommunication(self):
        if __name__ == "__main__":

            comms = Communication(self.com_name, self.__baudrate)
            comms.clear()  # just in case any junk is in the pipes
            while (True):
                comms.send_message("active")  # begin sending data
    def startComms(self):
        if __name__ == "__main__":
            self.numSamples = 250  # 5 seconds of data @ 50Hz
            self.refresh_time = 0.1  # update the plot every 0.1s (10 FPS)

            times = CircularList([], self.numSamples)  # Original 4 lists
            ax = CircularList([], self.numSamples)
            ay = CircularList([], self.numSamples)
            az = CircularList([], self.numSamples)

            average_x = CircularList([], self.numSamples)  # New 5 lists

            comms = Communication(self.com_name, self.__baudrate)
            comms.clear()  # just in case any junk is in the pipes
            comms.send_message("wearable")  # begin sending data

            #moveThresh = 60  # threshold for whats considered movement
            #avgThresh = 1  # threshold for acceptable average

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
                        currAvg = sum(ax) / np.count_nonzero(ax)
                        average_x.add(currAvg)


                        # find when we have moved within last 5 seconds
                        # if any point is greater than the average+some threshold
                        # ottherwise we havent moved
                        if ((ax[-1] > (currAvg + self.__moveThresh)) or (ax[-1] < (currAvg - self.__moveThresh))):
                            comms.send_message("active")
                            # print("a")
                        # case where inactive
                        if (abs(average_x[0] - average_x[-1]) < self.__avgThresh):
                            comms.send_message("inactive")
                            # print("b")
                        # print(abs(average_x[0]-average_x[-1]))
                        # if enough time has elapsed, clear the axis, and plot az
                        current_time = time()
                        if (current_time - previous_time > self.refreshTime):
                            previous_time = current_time
                            plt.cla()
                            plt.plot(ax, label='ax', color='red')
                            # plt.plot(ay, label='ay', color='blue')
                            # plt.plot(az, label='az', color='green')

                            plt.plot(average_x, label='average_x', color='cyan')
                            # plt.plot(delta_x, label='delta_x', color='magenta')
                            # plt.plot(L2, label='L2', color='yellow')
                            # plt.plot(L1, label='L1', color='black')
                            # plt.plot(transformed, label='distance', color='grey')

                            plt.show(block=False)
                            plt.pause(0.001)
            except(Exception, KeyboardInterrupt) as e:
                print(e)  # Exiting the program due to exception
            finally:
                comms.send_message("sleep")  # stop sending data
                comms.close()

    def getBaud(self):
        return self.__baudrate

    def setBaud(self,baudrate):
        self.__baudrate=baudrate

    def getName(self):
        return self.com_name

    def setName(self, com_name):
        self.com_name=com_name

    def getNumSamples(self):
        return self.numSamples

    def setNumSamples(self, numSamples):
        self.numSamples=numSamples

    def getRefreshTime(self):
        return self.refreshTime

    def setRefreshTime(self, refreshTime):
        self.refreshTime=refreshTime

    def getMoveThresh(self):
        return self.__moveThresh

    def setMoveThresh(self, moveThresh):
        self.__moveThresh=moveThresh

    def getAvgThresh(self):
        return self.__avgThresh

    def setAvgThresh(self, avgThresh):
        self.__avgThresh=avgThresh
