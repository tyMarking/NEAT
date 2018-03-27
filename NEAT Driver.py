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

import gzip;
import genotype, gene

def main():
    #stuff
    print("Main TODO")
    
    genome1 = []
    genome2 = []
    
    genome1.append(gene.Gene(1, 5, 0.5, True, 1))
    genome1.append(gene.Gene(2, 5, 0.5, True, 2))
    genome1.append(gene.Gene(3, 5, 0.5, True, 3))
    genome1.append(gene.Gene(4, 5, 0.5, True, 5))
    
    genome2.append(gene.Gene(1, 5, 1, True, 1))
#    genome2.append(gene.Gene(2, 5, 0.5, True, 2))
    genome2.append(gene.Gene(3, 5, 0.5, True, 3))
    genome2.append(gene.Gene(4, 6, 1.0, True, 4))
    

    genotype1 = genotype.Genotype(genome1)
    genotype2 = genotype.Genotype(genome2)
    
    print(genotype1.compatabilityDistance(genotype2, 1,2,3))


















"""
#read the MNIST data
print("Reading MNIST data")
trainImages = gzip.open("data/train-images-idx3-ubyte.gz", 'rb')
trainLabels = gzip.open("data/train-labels-idx1-ubyte.gz", 'rb')
imagesBytes = []


trainImages.read(16)
trainLabels.read(8)
trainData = []

#should be 60000
for i in range(100):
    image = []
    for pixle in trainImages.read(784):
        image.append(pixle/255)
    label = trainLabels.read(1)[0]
    trainData.append((image, label))

print("Finished reading MNIST data")

#Helper functions
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