# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:01:50 2018

@author: 136029
"""


"""
test set = [([ins], [label]),(i,l)...)]
"""
def fitnessFromSet(genotype, testSet, evalFunction):
    right = 0
    for test in testSet:
        inputs = test[0]
        label = test[1]
        
        if evalFunction(genotype, inputs) == label:
            right += 1
    
    return (right/len(testSet))