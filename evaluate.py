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
test set = [a1,a2,a3...]
"""
def evaluate(genotype, inputs):
    solvedNodes.clear()
    genome = genotype.connectGenome
    nodeGenome = genotype.nodeGenome

    #initial nodes
    for node in nodeGenome:
        if node.sensor:
            solvedNodes[node.nodeNum] = inputs[node.nodeNum - 1]
    
    outputs = []
    for node in nodeGenome:
        if node.output:
            outputs.append(solveNode(genome, inputs, node.nodeNum))
    
    return (outputs)

#to prevent loops by not solving for node already solving for
solvingFor = []
#using solvedNodes for dynamic programming
def solveNode(genome, inputs, nodeNum):
    #check if already solved
    if nodeNum in solvedNodes:
        return solvedNodes[nodeNum]
    #prevent loops
    if nodeNum in solvingFor:
        return 0
    else:
        solvingFor.append(nodeNum)
    
    #evaluate
    val = 0
    for geno in genome:
        if geno.outNode == nodeNum:
            val += geno.weight * solveNode(genome, inputs, geno.inNode)
    solvedNodes[nodeNum] = val
    solvingFor.pop()
    return val
            

