# import cv2
# import numpy as np
# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #==> use this instead if you’re on Windows!
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
# size = (width, height)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('capture.avi', fourcc, 20.0, size)
#
# while(True):
#   _, frame = cap.read()
#   edges=cv2.Canny(frame,100,200)
#   out.write(frame)
#   cv2.imshow('Input', edges)
#   c = cv2.waitKey(1)
#   if c == 27:
#     break
# cap.release()
# out.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
plt.style.use('seaborn-whitegrid')

ppg = []
timestamps= []

#cap = cv2.VideoCapture(0) # choose your appropriate camera!
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)# ==> use this instead if you’re on Windows!
while(True):
  _, frame = cap.read()
  new_sample = frame.mean(axis=0).mean(axis=0)
  new_sample = new_sample[2]  # replace the ? with index of the RED channel  openCV is in BGR format so b=0 g=1 r=2
  ppg.append(-1* new_sample)  # append new_sample to ppg
  timestamps.append(time.time_ns())
  cv2.imshow('Input', frame)
  c = cv2.waitKey(1)
  if c == 27:
    break
cap.release()
cv2.destroyAllWindows()

fig = plt.figure()
ax = plt.axes()
# p = ppg[10:] # remove the first few points because of auto-exposure
#
# x = np.linspace(0, 1, len(p))
# ax.plot(x, p)
# plt.show()
p = ppg[10:]
t = np.array(timestamps[10:]) # so we can easily subtract the first time
t = t - t[0]
t= t/(10**9)
ax.set_xlabel("time(s)")
ax.set_ylabel("Red Channel Value")

ax.plot(t, p)
plt.show()






