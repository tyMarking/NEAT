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
import gene
import genotype as Genotype
def evaluate(genotype, testSet):
    genome = genotype.genome
    
    #How determine end nodes??
    #for now:
    endNodeNums = [4]
    
    correct = 0
    
    for test in testSet:
        solvedNodes = {}
        
        #assuming input nodes are 1 to # of inputs
        for i in test[0]:
            solvedNodes[i] = test[0][i-1]
        
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


#using solvedNodes for dynamic programming
def solveNode(genome, inputs, nodeNum):
    
    if nodeNum in solvedNodes:
        return solvedNodes[nodeNum]
    val = 0
    for geno in genome:
        if geno.outNode == nodeNum:
            val += geno.weight * solveNode(genome, inputs, geno.inNode)
    solvedNodes[nodeNum] = val
    return val
            

testSet = [((1,2,3),3)]
genome = []

genome.append(gene.Gene(1, 4, 1.0, True, 1))
genome.append(gene.Gene(2, 4, 0.5, True, 2))
genome.append(gene.Gene(3, 4, 2, True, 3))
#    genome.append(gene.Gene(1, 5, 1.0, True, 4))
#    genome.append(gene.Gene(2, 5, 0.5, True, 5))
#    genome.append(gene.Gene(3, 5, 0.5, True, 6))
#    genome.append(gene.Gene(4, 6, 1.0, True, 7))

print(evaluate(Genotype.Genotype(genome), testSet))