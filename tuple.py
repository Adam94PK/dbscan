import numpy as np
import math as math
class Tuple:

    def __init__(self, args, classId = 0):
        self.classId = classId
        self.values = np.array(args)
        self.visited = False
        self.cluster = None
        self.type = None

    def getDistance(self, tuple):
        return math.sqrt(sum((self.values - tuple.values)**2))
