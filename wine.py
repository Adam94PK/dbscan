import tuple
import numpy as np
import math
import dbscan as db
import matplotlib.pyplot as plt
import sys, getopt

minPts = 16
eps = 2.7
opts, args = getopt.getopt(sys.argv[1:],"m:e:")
for o, a in opts:
    if o == '-m':
        minPts = float(a)
    elif o == '-e':
        eps = float(a)
    else:
        print("Usage: %s -m minPts -e eps" % sys.argv[0])

num_of_records = 178
num_of_atributes = 13
data = np.empty((num_of_records,num_of_atributes))
file = open("./wine.data", "r")
i = 0

for line in file:
    temp = line.split(',')
    temp = list(map(float, temp))
    #without 0 because it is class id
    data[i]=temp[1:]
    i+=1
file.close()
means = data.mean(0)
sd = []
for a in range(num_of_atributes):
    temp = 0
    for r in range(num_of_records):
        temp += (data[r][a] - means[a])**2
    sd.append(math.sqrt(temp/num_of_records))
for r in range(num_of_records):
    for a in range(num_of_atributes):
        data[r][a] = (data[r][a]-means[a])/sd[a]


data_set = []
for r in range(num_of_records):
    data_set.append(tuple.Tuple(data[r]))
print(data_set[0].values)

dbscan = db.Dbscan(data_set,minPts,eps)
clusters = dbscan.perform()

color = ['ro','go','bo', 'co', 'mo', 'yo', 'ko', 'wo','rs','gs','bs','cs', 'ms', 'ys', 'ks', 'ws','r^','g^', 'b^', 'c^', 'm^', 'y^', 'k^', 'w^', 'r*', 'g*', 'b*','c*', 'm*', 'y*', 'k*', 'w*']
i = 0
print("Liczba klastrow = " + str(len(clusters)))
for c in clusters:
    x = []
    y = []
    for t in c:
        x.append(t.values[4])
        y.append(t.values[5])
    plt.plot(x,y,color[i])
    i+=1
plt.show()

elements = 0
for c in clusters:
    elements += len(c)

print(elements)