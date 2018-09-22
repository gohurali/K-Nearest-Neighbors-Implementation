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
    for j in range(len(lines)):
        # print(lines[j][0])
        # print(lines[j][1])
        heights.append(lines[j][0])
        weights.append(lines[j][1])
        sizes.append(lines[j][2])
    
    # print(heights)
    # print(len(heights))
    # print(weights)
    # print(len(weights))
    # print(sizes)
    # print(len(sizes))

def euclideanDistance(class1, class2, height, weight):
    '''
    Lets assume lenth of data for class 1 == class 2
    Calculating the Euclidean Distance between two points
    ED = SQRT( (new-class1)^2 + (new-class2)^2 )
    :param: 
    :param: 
    '''
    distance = 0
    for x in range(class1):
        distance += ((pow( (height - class1[x]) ), 2) + (pow((weight - class2[x]),2)))
    return math.sqrt(distance)

def main():
    #num = euclideanDistance()
    #print(num)

    openCSV()
    pass

if __name__ == "__main__":
    main()