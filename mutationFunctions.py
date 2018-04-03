# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:06:30 2018

@author: 136029
"""
import random
import gene as Gene
import genetics

def standardMutate(genotype, weightProb, connectionProb, nodeProb):
    connections = genotype.connectGenome
    nodes = genotype.nodeGenome
    
    #weight mutations
    for connection in connections:
        if random.random() < weightProb:
            connection.weight += random.gauss(0, 1.5)
            
    #new connection
    for node in nodes:
        if random.random() < connectionProb:
            genetics.innovationNum += 1
            connections.append(Gene.ConnectGene(node.ndoeNum, random.choice(nodes).nodeNum, random.gauss(0, 2), True, genetics.innovationNum))
            
    #new node
    for connection in connections:
        if random.random() < nodeProb:
            connection.enabled = False
            genetics.nodeNumber += 1
            nodes.append(Gene.NodeGene(genetics.nodeNumber, False, False))
            genetics.innovationNum += 1
            connections.append(Gene.ConnectGene(connection.inNode, genetics.nodeNumber, connection.weight, True, genetics.innovationNumber))
            genetics.innovationNum += 1
            connections.append(Gene.ConnectGene(genetics.nodeNumber, connections.outNode, 1, True, genetics.innovationNumber))