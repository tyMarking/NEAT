# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 20:59:57 2018

@author: Ty
"""
import random, genotype

def crossover ( genoFit1, genoFit2):
    
    geno1 = genoFit1[0]
    geno2 = genoFit2[0]
    fit1 = genoFit1[1]
    fit2 = genoFit2[1]
    newNodeGenome = []
    newConnectGenome = []
    
    #node genomes
    i = 0
    j = 0
    while i < len(geno1.nodeGenome) and j < len(geno2.nodeGenome):
        if geno1.nodeGenome[i].nodeNum == geno2.nodeGenome[j].nodeNum:
            newNodeGenome.append(geno1.nodeGenome[i])
            i += 1
            j += 1
        else:
            if geno1.nodeGenome[i].nodeNum < geno2.nodeGenome[j].nodeNum:
                newNodeGenome.append(geno1.nodeGenome[i])
                i += 1
            else:
                newNodeGenome.append(geno2.nodeGenome[j])
                j += 1
                
    #excess from 2
    if i == len(geno1.nodeGenome) and j != len(geno2.nodeGenome):
        newNodeGenome += geno2.nodeGenome[j:]
    #Excess from 1
    elif j == len(geno2.nodeGenome) and i != len(geno1.nodeGenome):
        newNodeGenome += geno1.nodeGenome[i:]
        
        
    #connect Genomes
    i = 0
    j = 0
    while i < len(geno1.connectGenome) and j < len(geno2.connectGenome):   
        #if same gene
        if geno1.connectGenome[i].innovationNum == geno2.connectGenome[j].innovationNum:
            if random.choice((0,1)) == 0:
                newConnectGenome.append(geno1.connectGenome[i])
            else:
                newConnectGenome.append(geno2.connectGenome[j])
            
            i += 1
            j += 1
        else:
            if geno1.connectGenome[i].innovationNum < geno2.connectGenome[j].innovationNum:
                i += 1
                if fit1 >= fit2 and i < len(geno1.connectGenome):
                    newConnectGenome.append(geno1.connectGenome[i])
            else:
                j += 1
                if fit2 >= fit1 and j < len(geno2.connectGenome):
                    newConnectGenome.append(geno2.connectGenome[j])
    #Excess from 2
    if i == len(geno1.connectGenome) and j <len(geno2.connectGenome) and fit2 >= fit1:
        newConnectGenome += geno2.connectGenome[j:]
    #Excess from 1
    elif j == len(geno2.connectGenome) and i < len(geno1.connectGenome) and fit1 >= fit2:
        newConnectGenome += geno1.connectGenome[i:]
        
        
    return genotype.Genotype(newConnectGenome, newNodeGenome)