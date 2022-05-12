from ECE16Lib.HRMonitor import HRMonitor
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def eval_hr_monitor():
    ground_truth = np.array([73,72,71,70,71])
    hr_monitor = HRMonitor(3000, 50)
    #hr_monitor.adjustThreshold(0.5)

    dataA = np.genfromtxt("./data/a16568617_01_73.csv", delimiter=",")
    dataB = np.genfromtxt("./data/a16568617_02_72.csv", delimiter=",")
    dataC = np.genfromtxt("./data/a16568617_03_71.csv", delimiter=",")
    dataD = np.genfromtxt("./data/a16568617_04_70.csv", delimiter=",")
    dataE = np.genfromtxt("./data/a16568617_05_71.csv", delimiter=",")

    tA = dataA[:, 0]
    tA = (tA - tA[0]) / 1e3
    ppgA = dataA[:, 1]

    tB = dataB[:, 0]
    tB = (tB - tB[0]) / 1e3
    ppgB = dataB[:, 1]

    tC = dataC[:, 0]
    tC = (tC - tC[0]) / 1e3
    ppgC = dataC[:, 1]

    tD = dataD[:, 0]
    tD = (tD - tD[0]) / 1e3
    ppgD = dataD[:, 1]

    tE = dataE[:, 0]
    tE = (tE - tE[0]) / 1e3
    ppgE = dataE[:, 1]


    hr_monitor.add(tA,ppgA)
    hrA, peaks, filtered = hr_monitor.process()
    hr_monitor.reset()

    hr_monitor.add(tB, ppgB)
    hrB, peaks, filtered = hr_monitor.process()
    hr_monitor.reset()

    hr_monitor.add(tC, ppgC)
    hrC, peaks, filtered = hr_monitor.process()
    hr_monitor.reset()

    hr_monitor.add(tD, ppgD)
    hrD, peaks, filtered = hr_monitor.process()
    hr_monitor.reset()

    hr_monitor.add(tE, ppgE)
    hrE, peaks, filtered = hr_monitor.process()
    hr_monitor.reset()

    estimates=np.array([round(hrA),round(hrB),round(hrC),round(hrD),round(hrE)])

    print("True: ", ground_truth)
    print("Estimates: ", estimates)
    #print("-")


    return ground_truth, estimates



#ground_truth = # reference heart rates
#estimates =    # estimated heart rates from your algorithm

ground_truth, estimates = eval_hr_monitor()


[R,p] = stats.pearsonr(ground_truth, estimates) # correlation coefficient

plt.figure(1)
plt.clf()

# Correlation Plot
plt.subplot(211)
plt.plot(estimates, estimates)
plt.scatter(ground_truth, estimates)

plt.ylabel("Estimated HR (BPM)")
plt.xlabel("Reference HR (BPM)")
plt.title("Correlation Plot: Coefficient (R) = {:.2f}".format(R))

# Bland-Altman Plot
avg = ((ground_truth+estimates))/2# take the average between each element of the ground_truth and
      # estimates arrays and you should end up with another array
dif = (ground_truth-estimates)# take the difference between ground_truth and estimates
std = np.std(dif)# get the standard deviation of the difference (using np.std)
bias = np.mean(dif)# get the mean value of the difference
upper_std = bias+ (1.96 * std)# the bias plus 1.96 times the std
lower_std = bias- (1.96 * std)# the bias minus 1.96 times the std

plt.subplot(212)
plt.scatter(avg, dif)

plt.plot(avg, len(avg)*[bias])
plt.plot(avg, len(avg)*[upper_std])
plt.plot(avg, len(avg)*[lower_std])

plt.legend(["Mean Value: {:.2f}".format(bias),
  "Upper bound (+1.96*STD): {:.2f}".format(upper_std),
  "Lower bound (-1.96*STD): {:.2f}".format(lower_std)
])

plt.ylabel("Difference between estimates and ground_truth (BPM)")
plt.xlabel("Average of estimates and ground_truth (BPM)")
plt.title("Bland-Altman Plot")
plt.show()



# # Load the data as a 500x2 ndarray and extract the 2 arrays
# data = np.genfromtxt("./data/ramsink_01_13.csv", delimiter=",")
# t = data[:,0]
# t = (t - t[0])/1e3
# ppg = data[:,1]
#
# # Test the Heart Rate Monitor with offline data
# hr_monitor = HRMonitor(500, 50)
# hr_monitor.add(t, ppg)
# hr, peaks, filtered = hr_monitor.process()
#
# # Plot the results
# plt.plot(t, filtered)
# plt.title("Estimated Heart Rate: {:.2f} bpm".format(hr))
# plt.plot(t[peaks], filtered[peaks], 'rx')
# plt.plot(t, [0.6]*len(filtered), "b--")
# plt.show()

eval_hr_monitor()