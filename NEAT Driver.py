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
import genotype


def main():
    #stuff
    print("Main TODO")
    
    genome1 = []
    genome2 = []
    
    genotype1 = genotpye.Genotype(genome1)
    genotype2 = genotpye.Genotype(genome2)


















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