from ECE16Lib.Pedometer import Pedometer
import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    return np.genfromtxt(filename, delimiter=",")


# Load the data as a 500x4 ndarray
#data = load_data("./data/8steps_10s_50hz.csv")
#data=load_data("./data/accelerometer.csv")
data= load_data("./data/classMateMovement.csv")
t = data[:, 0]
t = (t - t[0]) / 1e3
ax = data[:, 1]
ay = data[:, 2]
az = data[:, 3]

# Test the Pedometer with offline data
ped = Pedometer(1500, 50, [])
ped.add(ax, ay, az)
ped.adjust_thresholds(15,30) #threshold check for walking
#ped.adjust_thresholds(58,95) #threshold check for jumping
#ped.adjust_thresholds(35,95)
steps, peaks, filtered = ped.process()

# Plot the results
plt.plot(t, filtered)
plt.title("Detected Peaks = %d" % steps)
plt.plot(t[peaks], filtered[peaks], 'rx')
plt.plot(t, [ped.get_low()] * len(filtered), "b--")
plt.plot(t, [ped.get_high()] * len(filtered), "b--")
plt.show()
