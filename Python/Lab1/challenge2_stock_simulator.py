import numpy as np

# Daily Apple Stock Value from 01-01-2019 - 04-30-2019
apple_stock = [
    38.38222885, 34.55907822, 36.03437042, 35.95417023, 36.63956451, 37.26177216, 37.38086700, 37.01386261,
    36.45728683, 37.20344162, 37.65793991, 37.88154221, 38.11487198, 37.25934601, 37.41003036, 37.11351776,
    38.34333038, 37.98849106, 37.59475327, 40.16376877, 40.45300674, 40.47245026, 41.62205887, 42.33419800,
    42.34877777, 41.54671860, 41.59553528, 41.35632706, 41.71270752, 41.53939438, 41.69073868, 41.59797287,
    41.72246552, 41.99096680, 41.75419617, 42.22041702, 42.52796555, 42.55237579, 42.68418503, 42.26435089,
    42.70859909, 42.92338943, 42.84527588, 42.59875488, 42.10569000, 42.20576477, 43.66787338, 44.15849686,
    44.35376358, 44.84682083, 45.43020248, 45.89398193, 45.53028870, 45.92815399, 47.61970139, 46.63357544,
    46.06971741, 45.59374619, 46.00382233, 46.06484222, 46.36507416, 46.67995834, 47.35852432, 47.68317032,
    47.76615143, 48.08591461, 48.84260559, 48.69614792, 48.96952438, 48.56189346, 48.54235840, 48.63023376,
    48.63512039, 49.58219528, 49.76038361, 49.92391968, 50.64399338, 50.56588364, 50.10699081, 49.86777878,
    49.94344711
]

strategy=np.zeros(81)


for x in range(len(apple_stock)):
    if x>=3:
        #Take previous 3 day average
        threeDay = apple_stock[x - 3]
        twoDay = apple_stock[x - 2]
        oneDay = apple_stock[x - 1]
        avg = (threeDay + twoDay + oneDay) / 3

        #Case where today is less than avg: sell
        if (avg < apple_stock[x]):
            strategy[x]= -1
        #Case where today is more than avg: buy
        elif (avg > apple_stock[x]):
            strategy[x]=1
        #Case where today and avg are the same: do nothing
        else:
            strategy[x]=0
    #Case where we are in day 1,2,3: do nothing
    else:
        strategy[x]=0

print(strategy)

#loop through our strategy array and calculate profits by sold*price that day= earn and buy*price that day= lost
profits=0
for idx,val in enumerate(strategy):
    profits += -1*val* apple_stock[idx]

print("Profits:", profits)


#loop through our strategy and add 1 for buying and subtract one for selling
shares=100
for x in strategy:
    shares+=x

print("Shares:",shares)
