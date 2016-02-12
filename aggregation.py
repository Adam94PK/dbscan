import tuple
import dbscan as db
import matplotlib.pyplot as plt
import sys, getopt

'''
Setup MinPts and eps
'''
minPts = 10
eps = 1.5
opts, args = getopt.getopt(sys.argv[1:],"m:e:")
for o, a in opts:
    if o == '-m':
        minPts = float(a)
    elif o == '-e':
        eps = float(a)
    else:
        print("Usage: %s -m minPts -e eps" % sys.argv[0])
print(minPts)
print(eps)

'''
Read data
'''
data = []
file = open("./aggregation.txt", "r")
#i =0
for line in file:
    temp = line.split('\t')
    temp = list(map(float, temp))
    temp.pop()
    data.append(tuple.Tuple(temp))
    #i+=1
    #if i==5000: break
file.close()

'''
Dbscan
'''
print("start dbscan")
dbscan = db.Dbscan(data,minPts,eps)
clusters = dbscan.perform()
print("start drawing")
i = 0
print("Liczba klastrow = " + str(len(clusters)))

'''
Print Dbscan output
'''

color = ['ro','go','bo', 'co', 'mo', 'yo', 'ko', 'wo','rs','gs','bs','cs', 'ms', 'ys', 'ks', 'ws','r^','g^', 'b^', 'c^', 'm^', 'y^', 'k^', 'w^', 'r*', 'g*', 'b*','c*', 'm*', 'y*', 'k*', 'w*']
plt.figure(1)
x = []
y = []
for d in data:
    x.append(d.values[0])
    y.append(d.values[1])
plt.subplot(211)
plt.title("Before DBSCAN")
plt.plot(x,y,color[1])

plt.subplot(212)
plt.title("After DBSCAN")
for c in clusters:
    x = []
    y = []
    for t in c:
        x.append(t.values[0])
        y.append(t.values[1])
    plt.plot(x,y,color[i])
    i+=1
plt.show()