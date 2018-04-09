# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:01:50 2018

@author: 136029
"""


"""
test set = [([ins], [label]),(i,l)...)]
"""
def MNISTFitnessFromSet(genotype, testSet, evalFunction):
    right = 0
    for test in testSet:
        inputs = test[0]
        label = test[1][0]
        """
        if evalFunction(genotype, inputs) == label:
            right += 1
            """
        evaluation = evalFunction(genotype, inputs)
        maxIndex = 0
        for i in range(1, len(evaluation)):
            if evaluation[i] > evaluation[maxIndex]:
                maxIndex = i
        
        if maxIndex == label:
            right += 1
    return (right/len(testSet))