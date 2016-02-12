import tuple
import dbscan as db
import matplotlib.pyplot as plt

data = []
file = open("./shapes.txt", "r")
i =0
for line in file:
    temp = line.split(' ')
    temp = list(map(float, temp))
    data.append(tuple.Tuple(temp))
    i+=1
    if i==2000: break
file.close()
print("start dbscan")
dbscan = db.Dbscan(data,10,14)
clusters = dbscan.perform()
print("start drawing")
color = ['ro','go','bo', 'co', 'mo', 'yo', 'ko', 'wo','rs','gs','bs','cs', 'ms', 'ys', 'ks', 'ws','r^','g^', 'b^', 'r*', 'g*', 'b*']
i = 0
print("Liczba klastrow = " + str(len(clusters)))
for c in clusters:
    x = []
    y = []
    for t in c:
        x.append(t.values[0])
        y.append(t.values[1])
    plt.plot(x,y,color[i])
    i+=1
plt.show()