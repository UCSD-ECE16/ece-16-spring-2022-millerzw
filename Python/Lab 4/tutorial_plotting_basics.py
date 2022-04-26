import matplotlib.pyplot as plt
x = [1,2,3,4]  # x data vector (as a list)
y = [1,4,9,16] # y data vector (as a list)
plt.clf()      # clear any existing plot
plt.plot(x,y)  # write the data onto the figure buffer
plt.show()     # show the figure

import numpy as np
a = np.array([[1,2,3,4],[1,4,9,16]])
plt.clf()
plt.plot(a)
plt.show()
# 4 lines were plotted, it takes the first dimension of the array as the first point and the 2nd as
# the second. THis prints a line from 1 to 1, 2 to 4, 3 to 9...etc

a = np.array([[1,2,3,4],[1,4,9,16]])
x = a[0,:] #index from a to get [1,2,3,4]
y = a[1,:] #index from a to get [1,4,9,16]
plt.title("First plot!")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,x)
plt.plot(x,y)
plt.show()

plt.clf()
plt.subplot(211)
plt.plot([1,2,3,4],[1,4,9,16])
plt.subplot(212)
plt.plot([1,2,3,4],[4,2,1,6])
plt.show()



