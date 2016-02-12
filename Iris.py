import tuple
import dbscan as db
import matplotlib.pyplot as plt

data=[]
file = open("./iris.data", "r")
for line in file:
    temp = line.split(',')
    temp.pop()
    temp = list(map(float, temp))
    data.append(tuple.Tuple(temp))
file.close()
i = 0
for tuple in data:
    i+=1
    print( str(i) + " " +  str(tuple.values))

dbscan = db.Dbscan(data,4,0.4)
clusters = dbscan.perform()

color = ['ro','go','bo','rs','gs','bs','r^','g^', 'b^', 'r*', 'g*', 'b*']
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