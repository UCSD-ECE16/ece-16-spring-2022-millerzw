from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.Pedometer import Pedometer
from ECE16Lib.HRMonitor import  HRMonitor
from matplotlib import pyplot as plt
from time import time




if __name__ == "__main__":
    fs = 50  # sampling rate
    num_samples = 750  # 15 seconds of data @ 50Hz
    process_time = 1  # compute the heartbeat count every second

    hr_monitor = HRMonitor(num_samples, fs, [])
    hr_monitor.adjustThreshold(0.5)

    comms = Communication("COM4", 115200)
    comms.clear()  # just in case any junk is in the pipes
    comms.send_message("wearable")  # begin sending data
    sendHRM=0
    hr_monitor.train()
    print("Model trained")

    try:
        previous_time = time()
        while (True):
            message = comms.receive_message()
            if (message != None):
                try:
                    (m1, _, _, _, m2) = message.split(',')
                    #print(str(m1), str(m2))
                except ValueError:  # if corrupted data, skip the sample
                    continue

                # Collect data in the pedometer
                hr_monitor.add(int(m1), int(m2))

                # if enough time has elapsed, process the data and plot it
                current_time = time()
                if (current_time - previous_time > process_time):
                    previous_time = current_time
                    #hr, peaks, filtered = hr_monitor.processGMM()
                    #print("heart count: {:f}".format(hr))
                    hr_est = hr_monitor.predict()
                    #sendHRM=float(hr*1000)%100
                    sendHRM = hr_est
                    print(sendHRM)

                # we want to always send the heartbeat number, not just on the 1 second time
                comms.send_message("%2f"% sendHRM)


    except(Exception, KeyboardInterrupt) as e:
        print(e)  # Exiting the program due to exception
    finally:
        print("Closing connection.")
        comms.send_message("sleep")  # stop sending data
        comms.close()

