# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:06:30 2018

@author: 136029
"""
import random
import gene as Gene
import genetics
import genotype as Genotype

#is not copying, mutating in place (change?)
def standardMutate(genotype, weightProb, connectionProb, nodeProb):
    connections = genotype.connectGenome
    nodes = genotype.nodeGenome
    
    #weight mutations
    for connection in connections:
        if random.random() < weightProb:
            connection.weight += random.gauss(0, 0.5)
            
    #new connection
    if random.random() < connectionProb:
        node = random.choice(nodes)
        genetics.innovationNumber += 1
        newGene = Gene.ConnectGene(node.nodeNum, random.choice(nodes).nodeNum, random.gauss(0, 2), True, genetics.innovationNumber)
        connections.append(newGene)
            
    #new node
    if random.random() < nodeProb:
        connection = random.choice(connections)
        connection.enabled = False
        genetics.nodeNumber += 1
        nodes.append(Gene.NodeGene(genetics.nodeNumber, False, False))
        genetics.innovationNumber += 1
        connections.append(Gene.ConnectGene(connection.inNode, genetics.nodeNumber, connection.weight, True, genetics.innovationNumber))
        genetics.innovationNumber += 1
        connections.append(Gene.ConnectGene(genetics.nodeNumber, connection.outNode, 1, True, genetics.innovationNumber))
    return Genotype.Genotype(connections, nodes)