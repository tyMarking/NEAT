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

import random

"""
speceis = [1,2,5,etc]
"""
def runGeneration(population, c1,c2,c3,compatabilityThreshold, fitnessFunction, maxMarker):
   
    print("Running Generation")
    #Seperate into Species
    #NEED TO TEST
    species = []
    species.append[population[0]]
    for geno in population[1:]:
        for speci in species:
            delta = geno.compatabilityDistance(random.choic(speci))
            if delta < compatabilityThreshold:
                speci.append(geno)
                break
        else:
            #was not assigned to a species
            species.append([geno])
            
    speciesWEval = []
    for speci in species:
        speci = []
        for geno in speci:
            speci.append((geno, fitnessFunction(geno)))
        speciesWEval.append(speci)
    
