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
    for i in range(len(genome.nodeGenome)):
        layers.append([])
    layerDict = layerEval(genome)
    #key = nodenum
    for key in layerDict:
        layer = layerDict[key]
        layers[layer].append(key)
    i = 0
    while i < len(layers):
        if layers[i] == []:
            del layers[i]
            i -= 1
        i += 1
    
    print(layers)
    
#for dynamic programing use
solvedNodes = {}

def layerEval(genotype):
    solvedNodes.clear()
    genome = genotype.connectGenome
    nodeGenome = genotype.nodeGenome

    #initial nodes
    for node in nodeGenome:
        if node.sensor:
            solvedNodes[node.nodeNum] = 0
    
#    outputs = []
    for node in nodeGenome:
        if node.output:
            solveNode(genome, node.nodeNum)
    
    return (solvedNodes)

#to prevent loops by not solving for node already solving for
solvingFor = []
#using solvedNodes for dynamic programming
def solveNode(genome, nodeNum):
    #check if already solved
    if nodeNum in solvedNodes:
        return solvedNodes[nodeNum]
    #prevent loops
    if nodeNum in solvingFor:
        return 0
    else:
        solvingFor.append(nodeNum)
    
    #evaluate
    minLayer = 0
    for geno in genome:
        if geno.outNode == nodeNum:
            x = solveNode(genome, geno.inNode)
            if minLayer < x:
                minLayer = x
    solvedNodes[nodeNum] = minLayer + 1
    solvingFor.pop()
    return minLayer + 1
    
    
    