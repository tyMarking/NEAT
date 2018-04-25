# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:27:10 2018

@author: Ty Marking


TODO:
    non-linear rectification fucntion (sigmoid probably)
    fix specieastion from killing new structures
        
    
    
    
    
"""

import gzip, json
import random
import copy
import fitnessFunctions, evaluate, matingFunctions, crossoverFunctions, mutationFunctions, genetics, gene, genotype

file1 = "FirstNEATv1.json"
file2 = "FirstNEATv2.json"
fileNum = 4
fileC = "FirstNEATv"+str(fileNum)+".json"

file = fileC
def main():
    
    #stuff
#    n = random.randint(0, 5899)
#    trainSet = trainData[n:n+100]
#    fitFunc = lambda x: fitnessFunctions.fitnessFromSet(x, trainSet, evaluate.evaluate)
    mateFunc = lambda speci, newNum : matingFunctions.mateTopR(speci, 25, newNum, crossoverFunctions.crossover)
    muteFunc = lambda geno: mutationFunctions.standardMutate(geno, 0.3, 10.5, 4.5)
#    genetics.runGeneration([/pop/], 1, 1, 3, 0.1, fitFunc, mateFunc, muteFunc)


#    pop = newPop(50)
#    print(pop)
    pop = loadFromFile(file)
    saveToFile(pop, file)

#    currentError = 1
    while True:
        
#        n = random.randint(0, 5899)
        n = 0
        trainSet = trainData[n:n+100]
        fitFunc = lambda x: fitnessFunctions.MNISTFitnessFromSet(x, trainSet, evaluate.evaluate)
        nextPop, maxFit = genetics.runGeneration(pop, 1000, 1000, 1,1, fitFunc, mateFunc, muteFunc)
        print("Maximum Fitness: " + str(maxFit))
        pop = nextPop
        saveToFile(pop, file)












print("Reading MNIST Data")

#read the MNIST data
trainImages = gzip.open("data/train-images-idx3-ubyte.gz", 'rb')
trainLabels = gzip.open("data/train-labels-idx1-ubyte.gz", 'rb')
imagesBytes = []


trainImages.read(16)
trainLabels.read(8)
trainData = []

#should be 60000
for i in range(60000):
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

#print("Finished reading MNIST data")

#Helper functions

def newPop(size):
    #created blank pop
    pop = []
    cGenome = []
    nGenome = []
    
    #input nodes
    genetics.innovationNumber = 0
    genetics.nodeNumber = 0
    for j in range(784):
        genetics.nodeNumber += 1
        nGenome.append(gene.NodeGene(genetics.nodeNumber, True, False))
        for k in range(10):
            genetics.innovationNumber += 1
            cGenome.append(gene.ConnectGene(genetics.nodeNumber, 785+k, random.gauss(0,1), True, genetics.innovationNumber))
    #output nodes
    for k in range(10):
        genetics.nodeNumber += 1
        nGenome.append(gene.NodeGene(genetics.nodeNumber, False, True))

    
    baseGeno = genotype.Genotype(cGenome, nGenome)
    for i in range(size):
        print(i)
        pop.append(copy.deepcopy(baseGeno))
    return pop

def saveToFile(pop, file):
    """
    netList = []
    for layer in net:
        netList.append((layer[0].tolist(),layer[1].tolist()))
        """
    popList = []
    for geno in pop:
        connectGList = []
        nodeGList = []
        for connectGene in geno.connectGenome:
            #inNode, outNode, weight, enabled, innovationNum
            connectGList.append((connectGene.inNode, connectGene.outNode, connectGene.weight, connectGene.enabled, connectGene.innovationNum))
        for nodeGene in geno.nodeGenome:
            #nodeNum, sensor, output
            nodeGList.append((nodeGene.nodeNum, nodeGene.sensor, nodeGene.output))
        popList.append( (connectGList, nodeGList) )
    popJson = json.dumps(popList)
    file = open(file, "w")
    file.truncate(0)
    file.write(popJson)

def loadFromFile(file):

    file = open(file, "r")
    popJson = file.read()
    popList = json.loads(popJson)
    pop = []
    for genoList in popList:
        connectGenome = []
        nodeGenome = []
        for cGT in genoList[0]:
            connectGenome.append(gene.ConnectGene(cGT[0],cGT[1],cGT[2],cGT[3],cGT[4]))
        for nGT in genoList[1]:
            nodeGenome.append(gene.NodeGene(nGT[0],nGT[1],nGT[2]))
        pop.append(genotype.Genotype(connectGenome, nodeGenome))
    return pop
    
    """matrixList = []
    for layer in netList:
        matrixList.append((np.matrix(layer[0]),np.matrix(layer[1])))
    return matrixList"""






main()