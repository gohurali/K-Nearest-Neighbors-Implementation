import numpy as np
import math
import csv
import pandas
import operator
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

def euclideanDistance(instance1, instance2, length):
    '''
    Lets assume lenth of data for class 1 == class 2
    Calculating the Euclidean Distance between two points
    ED = SQRT( (new-class1)^2 + (new-class2)^2 )
    '''
    distance = 0
    for i in range(length):
        distance += pow((int(instance1[i]) - int(instance2[i])),2)
    return math.sqrt(distance)

    
def getNeighbors(trainingSet, test_instance, k):
    '''
    :param:
    :param:
    '''
    distances = []
    # Get the length of the test set
    length = (len(test_instance)) - 1

    # Iterate through the training set
    for x in range(len(trainingSet)):
        dist = euclideanDistance(trainingSet[x], test_instance, length)
        distances.append((trainingSet[x], dist))
    
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def get_response(neighbors):
    class_votes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if(response in class_votes):
            class_votes[response] += 1
        else:
            class_votes[response] = 1
    sortedVotes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def get_accuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if(testSet[x][-1] is predictions[x]):
            correct += 1
    return (correct/float(len(testSet))) * 100

def main():
    #num = euclideanDistance()
    #print(num)

    training_set = []
    test_set = []
    split = 0.67

    # Open the CSV file and get arrays of data
    openCSV(split, training_set, test_set)

    print("training set")
    print(training_set)
    print()
    print('testing set')
    print(test_set)
    print()
    k = 3
    predictions = []
    for x in range(len(test_set)):
        neighbor = getNeighbors(training_set, test_set[x], k)
        print(neighbor)
        result = get_response(neighbor)
        predictions.append(result)
        print('> predicted=', result, ', actual=', test_set[x][-1])
    accuracy = get_accuracy(test_set, predictions)
    print('Accuracy: ', accuracy, '%')
    
    pass

if __name__ == "__main__":
    main()