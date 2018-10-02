import numpy as np
import math
import csv
import pandas
import random
'''
New Data:
Height: 161 cm
Weight: 61 kg
'''

def openCSV(split, training_set=[], test_set=[]):
    '''
    :param: split -- 0.67 standard split ratio
    :param: training_set array auto init'd
    :param: test_set array autho init'd 
    '''
    csv_data = csv.reader(open('heightToShirtSize.csv','r'))
    lines = list(csv_data)
    cols = lines[0]
    num_of_cols = len(cols)

    for j in lines[1:]:
        
        if(random.random() < split):
            training_set.append(j)
        else:
            test_set.append(j)

        # heights.append( int(j[0]) )
        # weights.append( int(j[1]) )
        # sizes.append(j[2] )

def euclideanDistance(class1, class2, height, weight):
    '''
    Lets assume lenth of data for class 1 == class 2
    Calculating the Euclidean Distance between two points
    ED = SQRT( (new-class1)^2 + (new-class2)^2 )
    :param: class1
    :param: class2
    :param: height
    :param: weight
    '''
    distance = 0
    distances = []
    for x in range(len(class1)):
        distance += (( pow( (height - int(class1[x])), 2) + (pow((weight - int(class2[x])),2))))
        distances.append(math.sqrt(distance))
    return distances

def getNeighbors(k):
    '''
    :param:
    :param:
    '''
    return

def main():
    #num = euclideanDistance()
    #print(num)

    training_set = []
    test_set = []
    split = 0.67

    # Open the CSV file and get arrays of data
    openCSV(split, training_set, test_set)

    print(training_set)
    print()
    print(test_set)

    # Calculate the Euclidean Distance for each data point compared to the new data point
    pass

if __name__ == "__main__":
    main()