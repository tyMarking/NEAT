# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:31:16 2018

@author: Ty Marking
"""

class ConnectGene():
    inNode = 0
    outNode = 0
    weight = 0
    innovationNum = 0
    enabled = False
    def __init__(self, inNode, outNode, weight, enabled, innovationNum):
        self.inNode = inNode
        self.outNode = outNode
        self.weight = weight
        self.enabled = enabled
        self.innovationNum = innovationNum
        
class NodeGene():
    nodeNum = 0
    sensor = False
    output = False
    
    def __init__(self, nodeNum, sensor, output):
        self.nodeNum = nodeNum
        self.sensor = sensor
        self.output = output
    