import tuple
import numpy as np
import matplotlib.pyplot as plt

class Dbscan:

    CORE, BORDER, NOISE = 1, 2, 3

    def __init__(self, data, minPts, eps):
        self.data = data
        self.minPts = minPts
        self.eps = eps
        self.clusters = []


    def getNeighbor(self, tuple):
        neighbor = []
        for p in self.data:
            if tuple.visited==False: continue
            if tuple.getDistance(p) < self.eps:
                neighbor.append(p)
        return neighbor

    def perform(self):
        for instance in self.data:
            if instance.visited==True:  continue

            instance.visited = True
            neighbour = self.getNeighbor(instance)

            if len(neighbour) < self.minPts:
                instance.type = self.NOISE
            else:
                cluster = neighbour+[instance]
                q = neighbour
                self.clusters.append(cluster)
                while len(q) > 0:
                    check_instance = q.pop()
                    #if check_instance.visited==True:  continue
                    check_instance.visited = True
                    neighbour = self.getNeighbor(check_instance)

                    if len(neighbour) < self.minPts:
                        check_instance.type = self.BORDER
                    else:
                        check_instance.type = self.CORE
                        for n in neighbour:
                            if n not in cluster:
                                cluster.append(n)
                                q.append(n)
        return self.clusters

