#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Artificial Intelligence
Collaborators:
    Keren Mitsue Ramírez Vergara
    Luis Arturo Banda Peláez
    Dr. Asdrúbal López Chau

Description: Selection Linear Classifier

Created on Wed Oct 13 16:00:39 2021

@author: arturop
"""

import random 
import numpy as np 
from population import Population
from fitness_function import FitnessFuction
class Selection:
    
    def __init__(self, ff):
        '''
        Constructor

        Parameters
        ----------
        ff : FitnessFuction
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.ff = ff

    def fitnessPopulation(self, population):
        '''
        Calculate a fitness function of every member

        Parameters
        ----------
        tag : dataframe
            DESCRIPTION. Classes or tags of the data
        values : dataframe
            DESCRIPTION. Set of selected data

        Returns
        -------
        list
            DESCRIPTION. List of aptitudes

        '''
        fitness = []
        for ind in population.getPopulation():
            fitness.append(self.ff.fitness(ind))
        return fitness
    
    
    def best(self, population):
        '''
        Get index best member

        Returns
        -------
        idxBest : int
            DESCRIPTION. Index of best member

        '''
        fitness = self.fitnessPopulation(population)
        idxBest = np.argmax(fitness)
        return idxBest
    
    
    def selectParentsIdx(self, population, numSelect=50):
        '''
        Select parents index

        Parameters
        ----------
        population : Population
            DESCRIPTION. Object Population
        numSelect : int, optional
            DESCRIPTION. The default is 50. Size of the selection of aptitudes to aech member

        Returns
        -------
        list
            DESCRIPTION. Index of selected the best members 

        '''
       # List of aptitudes
        aptitude = self.fitnessPopulation(population)
        aptitude = np.array(aptitude)
        a = np.min(aptitude)
        aptitude = aptitude - a
        ma = np.max(aptitude)
        if ma==0:
            ma = 1
            
        aptitude = aptitude/ma
        
        prob = np.exp(aptitude)/ np.sum(np.exp(aptitude))
        prob = list(prob)
        '''
        idxWorst = population.worst() # Worst aptitude
        aptitude = np.array(aptitude) # Convert list to array
        # Assigment probability
        aptitude = 1.-aptitude/idxWorst
        prob = np.exp(aptitude)/ np.sum(np.exp(aptitude))
        prob = list(prob)
        '''
        return random.choices(range(len(prob)), weights=prob, k=numSelect)
    
    def selectParents(self, population, numSelect=50):
        '''
        Select parents

        Parameters
        ----------
        population : Population
            DESCRIPTION. Object Population
        tag : dataframe
            DESCRIPTION. Classes or tags of the selected data
        values : dataframe
            DESCRIPTION. Values of the selected data set
        numSelect : int, optional
            DESCRIPTION. The default is 50. Size of the selection of aptitudes to aech member

        Returns
        -------
        parents : Population
            DESCRIPTION. Object Population (selected the best members)

        '''
        # Get index
        idxs = self.selectParentsIdx(population, numSelect)
        parents = Population(population.exampleMember, population.size)
        members = []
        # Append selected memebers
        for i in range (numSelect):
            members.append(population.getPopulation()[idxs[i]].copy())
        parents.setPopulation(members)
        return parents