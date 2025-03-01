from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.Pedometer import Pedometer
from ECE16Lib.HRMonitor import  HRMonitor
from matplotlib import pyplot as plt
from time import time
import cv2
import numpy as np
import time




if __name__ == "__main__":
    fs = 50  # sampling rate
    num_samples = 1500  # 30 seconds of data @ 50Hz
    process_time = 1  # compute the heartbeat count every second

    hr_monitor = HRMonitor(num_samples, fs, [])

    comms = Communication("COM4", 115200)
    comms.clear()  # just in case any junk is in the pipes
    comms.send_message("wearable")  # begin sending data
    sendHRM=0
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    try:
        previous_time = time.time()
        while (True):

            _,frame=cap.read()

            new_sample=frame.mean(axis=0).mean(axis=0)

            new_sample=new_sample[2]

            thisTime=time.time_ns() / (10**9)

            hr_monitor.add(int(thisTime), int(new_sample))



            current_time = time.time()
            if (current_time - previous_time > process_time):
                previous_time = current_time
                hr, peaks, filtered = hr_monitor.process()
                print("heart count: {:f}".format(hr))

                sendHRM = float(hr * 1000) % 100

          # we want to always send the heartbeat number, not just on the 1 second time
            comms.send_message("%2f" % sendHRM)


    except(Exception, KeyboardInterrupt) as e:
        print(e)  # Exiting the program due to exception
    finally:
        print("Closing connection.")
        comms.send_message("sleep")  # stop sending data
        comms.close()

