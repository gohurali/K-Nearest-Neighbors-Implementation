import numpy as np
import math

plot1 = [1,3]
plot2 = [2,5]

def euclideanDistance(instance1, instance2, length):
    '''
    Calculating the Euclidean Distance between two points
    :param: data_point1
    :param: data_point2
    '''
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(distance)