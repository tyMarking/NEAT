# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:27:10 2018

@author: Ty Marking


IDEAS:
    Main Loop:
        new batch
        seperate into species
        eval fitness
        determine grwoth/decline of species
        crossover
        
    
    
    
    
"""

import gzip
import random
import copy
import fitnessFunctions, evaluate, matingFunctions, crossoverFunctions, mutationFunctions, genetics, gene, genotype

def main():
    #stuff
    print("Main TODO")
#    n = random.randint(0, 5899)
#    trainSet = trainData[n:n+100]
#    fitFunc = lambda x: fitnessFunctions.fitnessFromSet(x, trainSet, evaluate.evaluate)
    mateFunc = lambda speci, newNum : matingFunctions.mateTopR(speci, 25, newNum, crossoverFunctions.crossover)
    muteFunc = lambda geno: mutationFunctions.standardMutate(geno, 0.3, 0.1, 0.03)
#    genetics.runGeneration([/pop/], 1, 1, 3, 0.1, fitFunc, mateFunc, muteFunc)


    #created blank pop
    pop = []
    cGenome = []
    nGenome = []
    
    #input nodes
    for j in range(10):
        nGenome.append(gene.NodeGene(j+1, True, False))
        cGenome.append(gene.ConnectGene(j+1, 11, random.gauss(0,1), True, j+1))
    #output nodes
    nGenome.append(gene.NodeGene(11, False, True))
    
    genetics.innovationNumber = 10
    genetics.nodeNumber = 11
    
    baseGeno = genotype.Genotype(cGenome, nGenome)
    for i in range(1000):
        pop.append(copy.deepcopy(baseGeno))
        
        

#    currentError = 1
    while True:
        
#        n = random.randint(0, 5899)
        n = 0
        trainSet = trainData[n:n+100]
        fitFunc = lambda x: fitnessFunctions.fitnessFromSet(x, trainSet, evaluate.evaluate)
        nextPop, maxFit = genetics.runGeneration(pop, 1, 1, 3, 4, fitFunc, mateFunc, muteFunc)
        print("Maximum Fitness: " + str(maxFit))













print("Reading MNIST Data")

#read the MNIST data
trainImages = gzip.open("data/train-images-idx3-ubyte.gz", 'rb')
trainLabels = gzip.open("data/train-labels-idx1-ubyte.gz", 'rb')
imagesBytes = []


trainImages.read(16)
trainLabels.read(8)
trainData = []

#should be 60000
for i in range(200):
    image = []
    for pixle in trainImages.read(784):
        image.append(pixle/255)
    label = trainLabels.read(1)[0]
    trainData.append((image, [label]))


testImages = gzip.open("data/t10k-images-idx3-ubyte.gz", 'rb')
testLabels = gzip.open("data/t10k-labels-idx1-ubyte.gz", 'rb')
imagesBytes = []

#testing data
testImages.read(16)
testLabels.read(8)
testData = []

#should be 10000
for i in range(100):
    image = []
    for pixle in testImages.read(784):
        image.append(pixle/255)
    label = testLabels.read(1)[0]
    testData.append((image, [label]))
print("Finished reading MNIST data")

print("Finished reading MNIST data")

#Helper functions
"""
def saveToFile(net, file):

    netList = []
    for layer in net:
        netList.append((layer[0].tolist(),layer[1].tolist()))
    netJson = json.dumps(netList)
    file = open(file, "w")
    file.truncate(0)
    file.write(netJson)

def loadFromFile(file):

    file = open(file, "r")
    netJson = file.read()
    netList = json.loads(netJson)
    matrixList = []
    for layer in netList:
        matrixList.append((np.matrix(layer[0]),np.matrix(layer[1])))
    return matrixList
"""





main()