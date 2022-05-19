from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.Pedometer import Pedometer
from matplotlib import pyplot as plt
from time import time
from ECE16Lib.HRMonitor import HRMonitor
import numpy as np
from pyowm import OWM
from datetime import date

import serial #the Pyserial library
#import time #for timing purposes

if __name__ == "__main__":
    fs = 50  # sampling rate
    num_samples = 250  # 5 seconds of data @ 50Hz
    process_time = 1  # compute the step count every second

    ped = Pedometer(num_samples, fs, [])
    hr_monitor = HRMonitor(num_samples, fs, [])

    comms = Communication("COM4", 115200)
    comms.clear()  # just in case any junk is in the pipes
    comms.send_message("wearable")  # begin sending data

    localSteps=0
    localBeats=0
    localWeather="booting"

    owm = OWM('fcc8e8f6ccdb6b424c31379ad974fb22').weather_manager()
    weather = owm.weather_at_place('San Diego,CA,US').weather

    try:
        previous_time = time()
        while (True):
            message = comms.receive_message()
            if (message != None):
                try:
                    (m1, m2, m3, m4, m5, m6) = message.split(',')
                    #m1= time
                    #m2-4 = accel
                    #m5= heartbeat
                    #m6=mode
                except ValueError:  # if corrupted data, skip the sample
                    continue

                # Collect data in the pedometer
                ped.add(int(m2), int(m3), int(m4))
                hr_monitor.add(int(m1), int(m5))

                # if enough time has elapsed, process the data and plot it
                current_time = time()
                if (current_time - previous_time > process_time):
                    previous_time = current_time

                    steps, peaks, filtered = ped.process()
                    hr, peaks, filtered = hr_monitor.process()

                    localSteps=steps;
                    localBeats=hr;

                    #plt.cla()
                    #plt.plot(filtered)
                    #plt.title("Step Count: %d" % steps)
                    #plt.show(block=False)
                    #plt.pause(0.001)
                    if (int(m6)==0):
                        #mode 1 temp
                        localWeather= str(weather.temperature('fahrenheit')).partition(",")[0]
                    else:
                        #mode 2 type eg. Sunny Cloudy etc.
                        localWeather= str(weather.detailed_status)
                comms.send_message(str(current_time)+"," + "Steps: "+str(localSteps)+"," + "Heartbeat: "+str(localBeats)+ ","+localWeather)


    except(Exception, KeyboardInterrupt) as e:
        print(e)  # Exiting the program due to exception
    finally:
        print("Closing connection.")
        comms.send_message("sleep")  # stop sending data
        comms.close()
