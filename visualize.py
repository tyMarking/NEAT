#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:31:28 2018

@author: tymarking
"""
import graphics as g

#layers = []
solvingFor = []
def viz(genome):
    layers = []
    outputNums = []
    for i in range(len(genome.nodeGenome)):
        layers.append([])
        if genome.nodeGenome[i].output:
            outputNums.append(genome.nodeGenome[i].nodeNum)
    layerDict = layerEval(genome)
    
    
    #key = nodenum
    for key in layerDict:
        layer = layerDict[key]
        if key in outputNums:
            layers[-1].append(key)
        else:
            layers[layer].append(key)
    i = 0
    while i < len(layers):
        if layers[i] == []:
            del layers[i]
            i -= 1
        i += 1
    
    print(layers)
#    drawLayers(layers, genome)
    
    
def drawLayers(layers, genome):
    width = 800
    height = 800
    win = g.GraphWin("Viz",width, height)
    xD = (width-100)/(len(layers)-1)
    currentX = 50
    nodePos = {}
    for layer in layers:
        if len(layer) == 1:
            nodeC = g.Circle(g.Point(currentX, height/2),10)  
            nodePos[layer[0]] = (currentX, height/2)
            nodeC.setFill("black")
            nodeC.draw(win)
        else:    
            yD = (height-100)/(len(layer)-1)
            currentY = 50
            for node in layer:
                nodeC = g.Circle(g.Point(currentX, currentY),10)    
                nodePos[node] = (currentX, currentY)
                nodeC.setFill("black")
                nodeC.draw(win)
                currentY += yD
        
        currentX += xD
        
    for connection in genome.connectGenome:
        if connection.inNode > 794 or connection.outNode > 794:
            inPos = nodePos[connection.inNode]
            outPos = nodePos[connection.outNode]
            
            cLine = g.Line(g.Point(inPos[0],inPos[1]), g.Point(outPos[0], outPos[1]))
            cLine.setWidth(abs(connection.weight * 2)+0.01)
            if connection.weight > 0:
                cLine.setFill("blue")
            elif connection.weight < 0:
                cLine.setFill("red")
            cLine.draw(win)
        
       
    print("spacer")
    win.getMouse()
    win.close()
    
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
    
    
    