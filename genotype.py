# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:31:32 2018

@author: Ty Marking
"""


class Genotype():
    genome = []
#    species = 0
    
    def __init__(self, genome):
        self.genome = genome
    
    
    
    def run(self, inputs):
        print("TODO")
        
#    def assignSpecies(self, species):
#        self.species = species
        
    def compatabilityDistance(self, other, c1,c2,c3):
        """
        δ = (c1E/N)+(c2D/N)+c3*ΔW
        """

        E = 0 #excess genes
        D = 0 #disjointed genes
        W = 0 #weight difference
        N = 0 #max number of genes
        
        # Max number of genes
        N = max(len(self.genome), len(other.genome))
        
       
        #excess and disjointed genes
        i = 0
        j = 0
        sameGenei = []
        sameGenej = []
        while i < len(self.genome) and j < len(other.genome):
            #if same gene move on
            if self.genome[i].innovationNum == other.genome[j].innovationNum:
                sameGenei.append(i)
                sameGenej.append(j)
                i += 1
                j += 1
            else:
                
                D +=1                
                if self.genome[i].innovationNum < other.genome[j].innovationNum:
                    i += 1
                else:
                    j += 1
        #Excess from other, ends loop
        if i == len(self.genome):
                    E = len(other.genome) - i
        #Excess from self, ends loop
        elif j == len(other.genome):
                    E = len(self.genome) - j
        #weight differences
        weightSum = 0
        for index in range(len(sameGenei)):
            weightSum += abs(self.genome[sameGenei[index]].weight - other.genome[sameGenej[index]].weight)
        if len(sameGenei) == 0:
            W = 0
        else:
            W = weightSum/len(sameGenei)
        
        
        distance = (c1*E)/N + (c2*D)/N + c3*W
        return distance
    
    
        