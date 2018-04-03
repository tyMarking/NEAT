# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:39:49 2018

@author: 136029
"""
import random

def mateTopR(species, r, newNum, crossoverFunc):
    parents = species[len(species)*int((r/100)):]
    newPop = []
    for i in range(newNum):
        newPop.append(crossoverFunc(random.choice(parents), random.choice(parents)))
    return newPop