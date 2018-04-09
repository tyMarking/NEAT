# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:32:25 2018

@author: Ty Marking

Main Loop:
        new batch
        seperate into species
        eval fitness
        determine grwoth/decline of species
        crossover


"""

import random, math
innovationNumber = 0
nodeNumber = 0
"""
speceis = [1,2,5,etc]
"""
def runGeneration(population, c1,c2,c3, compatabilityThreshold, fitnessFunction, mateFunction, muteFunction):
   
#    print("Running Generation")
    #Seperate into Species
    #NEED TO TEST
    species = []
#    print(population)
    species.append([population[0]])
    for geno in population[1:]:
        for speci in species:
            delta = geno.compatabilityDistance(random.choice(speci), c1,c2,c3)
            if delta < compatabilityThreshold:
                speci.append(geno)
                break
        else:
            #was not assigned to a species
            species.append([geno])
    print("Size of population: " + str(len(population)))
    print("Number of species: " + str(len(species)))
    #Evaluation
    #getting max fitness for return
    maxFit = 0
    #speciesWEval = [[(geno, fitness), (g, f)],[spec2],[spec3]...]
    speciesWEval = []
    for speci in species:
        speciVal = []
        for geno in speci:
            fitness = fitnessFunction(geno)
#            print("fitness: " + str(fitness))
            speciVal.append((geno, fitness))
            if fitness > maxFit:
                maxFit = fitness
                """
            if fitness != 0.13:
                for i in range(10):
                    print("LOOOOOOOOK ITS NOT 13")
            if len(geno.connectGenome) != 10 or len(geno.nodeGenome) != 11:
                for i in range(10):
                    print("LOOOOOOOOK STRUCTURE MUTATION")
                    """
        speciesWEval.append(speciVal)
    
    
    print("MaxFit inside gen: " + str(maxFit))
    
    
    #Grwoth/decline of species
    
    #adjusted fitness
    speciesWAdjEval = []
    for speci in speciesWEval:
        speciVal = []
        for genoFPair in speci:
            speciVal.append( (genoFPair[0], genoFPair[1]/len(speci)) )
        speciesWAdjEval.append(speciVal)
#    print(speciesWAdjEval)
    
    #mean adjusted fitness
    adjSum = 0
    count = 0
    for speci in speciesWAdjEval:
        for genoFPair in speci:
            adjSum += genoFPair[1]
            count += 1
    meanF = adjSum/count
    
    #mating
    unmutedPop = []
    for speci in speciesWAdjEval:
        adjSum = 0
        for genoFPair in speci:
            adjSum += genoFPair[1]
        newNum = int(math.ceil(adjSum/meanF))
        unmutedPop.append(mateFunction(speci, newNum))
    
    #mutating
    mutedPop = []
    for speci in unmutedPop:
        for pop in speci:
            mutedPop.append(muteFunction(pop))
            
    return(mutedPop, maxFit)
    