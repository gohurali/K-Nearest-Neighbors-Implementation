import numpy as np
import math
import csv
import pandas
'''
New Data:
Height: 161 cm
Weight: 61 kg
'''

def openCSV():
    csv_data = csv.reader(open('heightToShirtSize.csv','r'))
    lines = list(csv_data)
    cols = lines[0]
    num_of_cols = len(cols)

    heights = []
    weights = []
    sizes = []

    for j in lines[1:]:#range(len(lines[1:])):
        heights.append( int(j[0]) )
        weights.append( int(j[1]) )
        sizes.append(j[2] )
    
    print(heights)
    print(len(heights))
    print(weights)
    print(len(weights))
    print(sizes)
    print(len(sizes))
    return heights, weights, sizes

def euclideanDistance(class1, class2, height, weight):
    '''
    Lets assume lenth of data for class 1 == class 2
    Calculating the Euclidean Distance between two points
    ED = SQRT( (new-class1)^2 + (new-class2)^2 )
    :param: 
    :param: 
    '''
    distance = 0
    distances = []
    for x in range(len(class1)):
        distance += (( pow( (height - int(class1[x])), 2) + (pow((weight - int(class2[x])),2))))
        distances.append(math.sqrt(distance))
    
    
    return distances

def main():
    #num = euclideanDistance()
    #print(num)

    heights, weights, sizes = openCSV()
    nums = euclideanDistance(heights, weights, 161, 61)
    print(nums)
    print(len(nums))
    pass

if __name__ == "__main__":
    main()