# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 10:09:59 2018

@author: 136029
"""
import gene, genotype, evaluate, genetics, evaluate


def main():
#    evalTest()
    generationTest()



def generationTest():
    result = daveAndJane()
    dave = result[0]
    jane = result[1]
    print(jane)
    pop = [dave, jane]
    genetics.runGeneration(pop, 1,2,3, 0.1, evaluate.evaluate, 7)
    

def evalTest():
    testSet = [1,2,3]
    dave, jane = daveAndJane()
    
    print(evaluate.evaluate(dave, testSet))
    print(evaluate.evaluate(jane, testSet))
    print(dave.compatabilityDistance(jane, 1, 2, 3))
    #print(evaluate(Genotype.Genotype(genome), testSet))
    
    
    
def daveAndJane():
    cGenome1 = []
    nGenome1 = []
    
    #input nodes
    nGenome1.append(gene.NodeGene(1, True, False))
    nGenome1.append(gene.NodeGene(2, True, False))
    nGenome1.append(gene.NodeGene(3, True, False))
    
    #output nodes
    nGenome1.append(gene.NodeGene(4, False, True))
    
    #hidden nodes
    nGenome1.append(gene.NodeGene(5, False, False))
    
    #connections
    cGenome1.append(gene.ConnectGene(1, 4, 1.0, True, 1))
    cGenome1.append(gene.ConnectGene(2, 4, 0.5, True, 2))
    cGenome1.append(gene.ConnectGene(3, 4, 2, True, 3))
    cGenome1.append(gene.ConnectGene(1, 5, 1, True, 4))
    cGenome1.append(gene.ConnectGene(2, 5, 1, True, 5))
    cGenome1.append(gene.ConnectGene(5, 4, 1, True, 6))
    
    
    dave = genotype.Genotype(cGenome1, nGenome1)
    
    cGenome2 = []
    nGenome2 = []
    
    #input nodes
    nGenome2.append(gene.NodeGene(1, True, False))
    nGenome2.append(gene.NodeGene(2, True, False))
    nGenome2.append(gene.NodeGene(3, True, False))
    
    #output nodes
    nGenome2.append(gene.NodeGene(4, False, True))
    
    #hidden nodes
    nGenome2.append(gene.NodeGene(5, False, False))
    
    #connections
    cGenome2.append(gene.ConnectGene(1, 4, 1.0, True, 1))
    cGenome2.append(gene.ConnectGene(2, 4, 0.5, True, 2))
    cGenome2.append(gene.ConnectGene(3, 4, 2, True, 3))
    cGenome2.append(gene.ConnectGene(1, 5, 1, True, 4))
    cGenome2.append(gene.ConnectGene(2, 5, 1, True, 5))
    cGenome2.append(gene.ConnectGene(5, 4, 1, True, 6))
    cGenome2.append(gene.ConnectGene(3, 5, 1, True, 7))
    cGenome2.append(gene.ConnectGene(4, 5, 1, True, 8))
    
    jane = genotype.Genotype(cGenome2, nGenome2)
    
    return (dave, jane)
main()