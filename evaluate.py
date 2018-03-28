# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:31:40 2018

@author: Ty Marking
"""

"""

use dynamic programming, start from end and recursion down?
or start from begining and keep lookping through each layer?
what about loops?

"""
#for dynamic programing use
solvedNodes = {}


"""
test set = [(in, out),(in, out)...]
"""
def evaulate(genotype, testSet):
    genome = genotype.genome
    
    #How determine end nodes??
    #for now:
    endNodeNums = [4]
    
    correct = 0
    
    for test in testSet:
        solvedNodes = {}
        
        #assuming input nodes are 1 to # of inputs
        for i in test[0]:
            solvedNodes.add(i+1, test[0][i])
        
        outputs = []
        for num in endNodeNums:
            outputs.append(solveNode(genome, test[0], num))
        
        #get max output
        maxi = 0
        for i in range(1, len(outputs)):
            if outputs[i] > outputs[maxi]:
                maxi = i
                
        if maxi == testSet[0]:
            correct += 1

    return (correct/len(testSet))


#using solvedNodes for synamic programming
def solveNode(genome, inputs, nodeNum):
    
    if nodeNum in solvedNodes:
        return solvedNodes[nodeNum]
    val = 0
    for gene in genome:
        if gene.outNode == nodeNum:
            val += gene.weight * solveNode(genome, inputs, gene.inNode)
    solvedNodes.add(nodeNum, val)
    return val
            