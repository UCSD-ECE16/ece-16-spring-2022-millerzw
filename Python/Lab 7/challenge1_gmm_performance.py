# Import for searching a directory
import glob

# The usual suspects
import numpy as np
import ECE16Lib.DSP as filt
import matplotlib.pyplot as plt

# The GMM Import
from sklearn.mixture import GaussianMixture as GMM

# Import for Gaussian PDF
from scipy.stats import norm

#Import for RMSE
from sklearn.metrics import mean_squared_error

#Import for R^2
#This will show how much the variance between data points differs from true correlation
#ex 0.5 means ~half of the results can be explained from the ML model
from sklearn.metrics import r2_score

#Import for MAE (Mean Absolute Error)
#similar to rmse, this measures the average magnitude of error of the results as comapred to the true calues
from sklearn.metrics import mean_absolute_error

# Retrieve a list of the names of the subjects
def get_subjects(directory):
  filepaths = glob.glob(directory + "\\*")
  return [filepath.split("\\")[-1] for filepath in filepaths]

# Retrieve a data file, verifying its FS is reasonable
def get_data(directory, subject, trial, fs):
  search_key = "%s\\%s\\%s_%02d_*.csv" % (directory, subject, subject, trial)
  filepath = glob.glob(search_key)[0]
  t, ppg = np.loadtxt(filepath, delimiter=',', unpack=True)
  t = (t-t[0])/1e3
  hr = get_hr(filepath, len(ppg), fs)

  fs_est = estimate_fs(t)
  if(fs_est < fs-1 or fs_est > fs):
    print("Bad data! FS=%.2f. Consider discarding: %s" % (fs_est,filepath))

  return t, ppg, hr, fs_est

# Estimate the heart rate from the user-reported peak count
def get_hr(filepath, num_samples, fs):
  count = int(filepath.split("_")[-1].split(".")[0])
  seconds = num_samples / fs
  return count / seconds * 60 # 60s in a minute

# Estimate the sampling rate from the time vector
def estimate_fs(times):
  return 1 / np.mean(np.diff(times))

# Filter the signal (as in the prior lab)
def process(x):
  x = filt.detrend(x, 25)
  x = filt.moving_average(x, 5)
  #bl, al = filt.create_filter(3, 1, "lowpass", 50)  # Low-pass Filter Design
  #x = filt.filter(bl, al, x)  # Low-pass Filter Signal
  x = filt.gradient(x)
  return filt.normalize(x)

# Plot each component of the GMM as a separate Gaussian
def plot_gaussian(weight, mu, var):
  weight = float(weight)
  mu = float(mu)
  var = float(var)

  x = np.linspace(0, 1)
  y = weight * norm.pdf(x, mu, np.sqrt(var))
  plt.plot(x, y)

# Estimate the heart rate given GMM output labels
def estimate_hr(labels, num_samples, fs):
  peaks = np.diff(labels, prepend=0) == 1
  count = sum(peaks)
  seconds = num_samples / fs
  hr = count / seconds * 60 # 60s in a minute
  return hr, peaks

# Run the GMM with Leave-One-Subject-Out-Validation
if __name__ == "__main__":
  fs = 50
  directory = ".\\data"
  subjects = get_subjects(directory)

  actual=[0]*5
  estimates=[0]*5

  # Leave-One-Subject-Out-Validation
  # 1) Exclude subject
  # 2) Load all other data, process, concatenate
  # 3) Train the GMM
  # 4) Compute the histogram and compare with GMM
  # 5) Test the GMM on excluded subject
  for exclude in subjects:
    print("Training - excluding subject: %s" % exclude)
    train_data = np.array([])
    for subject in subjects:
      for trial in range(1,6):
        t, ppg, hr, fs_est = get_data(directory, subject, trial, fs)

        if subject != exclude:
          train_data = np.append(train_data, process(ppg))

    # Train the GMM
    train_data = train_data.reshape(-1,1) # convert from (N,1) to (N,) vector
    gmm = GMM(n_components=2).fit(train_data)

    # Compare the histogram with the GMM to make sure it is a good fit
    #plt.hist(train_data, 100, density=True)
    #plot_gaussian(gmm.weights_[0], gmm.means_[0], gmm.covariances_[0])
    #plot_gaussian(gmm.weights_[1], gmm.means_[1], gmm.covariances_[1])
    #plt.show()

    # Test the GMM on excluded subject
    print("Testing - all trials of subject: %s" % exclude)
    for trial in range(1,6):
      t, ppg, hr, fs_est = get_data(directory, exclude, trial, fs)
      test_data = process(ppg)

      labels = gmm.predict(test_data.reshape(-1,1))

      hr_est, peaks = estimate_hr(labels, len(ppg), fs)
      print("File: %s_%s: HR: %3.2f, HR_EST: %3.2f" % (exclude,trial,hr,hr_est))

      actual[trial-1]=hr
      estimates[trial-1]=hr_est

      #plt.plot(t, test_data)
      #plt.plot(t, peaks)
      #plt.show()

    rmse=mean_squared_error(actual, estimates, squared=False)
    r2= r2_score(actual,estimates)
    mae= mean_absolute_error(actual,estimates)
    #plt.plot(estimates, estimates)
    plt.scatter(actual, estimates)
    plt.ylabel("Estimated HR (BPM)")
    plt.xlabel("True HR (BPM)")
    plt.title("Coefficient (RMSE) = {:.2f}, Coefficient (R^2) = {:.2f}, Coefficient (MAE) = {:.2f}".format(rmse,r2,mae))
    plt.show()
    #print(rmse)



#show r^2 value
#show standard deviation
# https://towardsdatascience.com/ways-to-evaluate-regression-models-77a3ff45ba70 some other examples here to look at