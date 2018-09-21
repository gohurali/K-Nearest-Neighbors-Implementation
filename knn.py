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


    for j in range(len(lines)):
        j = j + 1
        print(lines[j][0])


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