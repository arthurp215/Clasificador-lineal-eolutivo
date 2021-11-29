# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Artificial Intelligence
Topic: Genetic Algorithms
Collaborators:
    Keren Mitsue Ramírez Vergara
    Luis Arturo Banda Peláez
    Dr. Asdrúbal López Chau
Description: Evolutionary Algorithm Linear Classifier

Created on Wed Oct 13 07:22:01 2021

@author: KerenMitsue
"""

from population import Population
from selection import Selection
from fitness_function import FitnessFuction
from plot_data import PlotData
import itertools

import numpy as np
import random

class AEvolution:

    def __init__(self, population=None,  fitnessFunction=None, selection=None, generations=100 ):
        '''
        Constructor

        Parameters
        ----------
        numAttr : int
            DESCRIPTION. Number or attributes
        maxValue : float
            DESCRIPTION. Max value of data
        tag : data frame
            DESCRIPTION. dataframe of classes
        values : data frame
            DESCRIPTION. dataframe attributes
        sizePopulation : int, optional
            DESCRIPTION. The default is 100. Size of population
        generations : int, optional
            DESCRIPTION. The default is 100. Number of interations

        Returns
        -------
        None.

        '''
        
        self.population = population
        self.sizePopulation = len(population.getPopulation())
        self.selection = selection
        self.ff = fitnessFunction
        self.generations = generations
        self.best = None
        
    def evole(self, generations=None):
        '''
        Does the Algorithm Evolutionary

        Returns
        -------
        None.

        '''
        if generations is not None:
            self.generations = generations
        indices = []
        for i in range (self.generations):
            print('Generation:', (i + 1))
            # Select fathers
            K = int(len(self.population.getPopulation())/2)
            father = self.selection.selectParents(self.population, K)
            mother = self.selection.selectParents(self.population, K)
            
            #Crossover with fathers and mothers
            descent = []
            for dad, mom in zip(father.getPopulation(), mother.getPopulation()):
                sonA, sonB = mom.crossover(dad)
                descent.append(sonA)
                descent.append(sonB)
                
            # Mutate to 20% of sons
            
            offspring = Population(self.population.exampleMember, self.population.size)
            offspring.setPopulation(descent)
            
            totalMutate = np.ceil(len(offspring.getPopulation()) * 0.3)
            
            for i in range(int(totalMutate)):
                x = random.randint(0, len(offspring.getPopulation()) - 1)
                offspring.getPopulation()[x].mutate()
            
            # Join fathers and sons
            generation = Population(self.population.exampleMember, self.population.size)
            generation.setPopulation(self.join(father, mother, offspring))
            #Elitism
            idx = self.selection.best(generation)
            best = generation.getPopulation()[idx].copy()
            fitnessBest = self.ff.fitness(best)
            if self.best is None:
                self.THEBEST = best.copy()
                self.best  = best.copy()
                self.bestFitness = fitnessBest
                
                print(self.best.getPhenotype())
                print(self.THEBEST.getPhenotype())
                print(self.bestFitness)
                gc = PlotData()
                gc.plot2D(self.ff.values.iloc[:, [0, 1]], self.ff.tag)
                gc.plotLine(self.best)
            
            if fitnessBest > self.bestFitness:
                self.THEBEST = best.copy()
                self.best  = best.copy()
                self.bestFitness = fitnessBest
                
                print(self.best.getPhenotype())
                print(self.THEBEST.getPhenotype())
                print(self.bestFitness)
                gc = PlotData()
                gc.plot2D(self.ff.values.iloc[:, [0, 1]], self.ff.tag)
                gc.plotLine(self.best)

            # Select the next generation
            generation = self.selection.selectParents(generation, self.sizePopulation - 1)
            generation.getPopulation().append(best)
            #generation.fitnessPopulation(self.tag, self.values)
            self.population.setPopulation(generation.getPopulation())

        # Ploat the best member
        print(self.best.getPhenotype())
        print(self.bestFitness)
        
            
    def join(self, father, mother, sons):
        '''
        Join generation

        Parameters
        ----------
        father : list 
            DESCRIPTION. List of fathers
        mother : list
            DESCRIPTION. List of mothers
        sons : list 
            DESCRIPTION. List of sons

        Returns
        -------
        ind : list
            DESCRIPTION. List of generation

        '''
        ind = []
        for i in father.getPopulation():
            ind.append(i)
        for i in mother.getPopulation():
            ind.append(i)
        for i in sons.getPopulation():
            ind.append(i)
        return ind
            
            