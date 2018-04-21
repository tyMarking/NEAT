#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:31:28 2018

@author: tymarking
"""
#layers = []
solvingFor = []
def viz(genome):
    layers = []
    inNodes = []
    outNodes = []
    
    for node in genome.nodeGenome:
        if node.sensor:
            inNodes.append(node)
        if node.output:
            outNodes.append(node)
    
    layers.append(inNodes)
    for node in genome.nodeGenome:
        solvingFor = []
        solveRec(node, genome, layers)
        
        
    #now have layers done?
    print(layers)

def solveRec(node, genome, layers):
    print(node.nodeNum)
    print(len(layers))
    
    
    if node in solvingFor:
        return
    toDo = True
    for layer in layers:
        if node in layer:
            toDo = False
    if node in solvingFor:
        toDo = False
    if toDo:
        solvingFor.append(node)
        reqs = []
        for connection in genome.connectGenome:
            

            if connection.outNode == node.nodeNum:
                reqs.append(connection.inNode)
            
        reqNodes = []
        for i in range(len(layers)):
            for lNode in layers[i]:
                if lNode.nodeNum in reqs:
                    reqNodes.append(lNode)
        
        minNeededLayer = 0
        for rNode in reqNodes:
            isLayered = False
            for i in range(len(layers)):
                isThere = False
                for layer in layers:
                    for iNode in layer:
                        if iNode.nodeNum == rNode.nodeNum:
                            isThere = True
                            break
                        
                if isThere:
                    if i > minNeededLayer:
                        minNeededLayer = i
                        isLayered = True
                        break
            if not isLayered:
                    solveRec(rNode, genome, layers)
            for i in range(len(layers)):
#                if node in layers[i]:
                for iNode in layers[i]:
                        if iNode.nodeNum == rNode.nodeNum:
                            if i > minNeededLayer:
                                minNeededLayer = i
                                break
                    
        #now should have minNeededLayer
        if minNeededLayer+1 >= len(layers):
            layers.append([node])
        else:
            layers[minNeededLayer+1].append(node)
        solvingFor.pop()
        return

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
    """
    
    