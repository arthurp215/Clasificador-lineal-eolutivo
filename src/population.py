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
Description: Population Linear Classifier

Created on Tue Oct 12 23:30:05 2021

@author: KerenMitsue
"""

class Population:
    
    def __init__(self, exampleMember, size=100):
        '''
        Builds a population with members similar to
        exampleMember

        Parameters
        ----------
        exampleMember : Member2
            DESCRIPTION. The structure of the
            instance is used as a example to create more 
            members.
            
        size : int, optional
            DESCRIPTION. Size of population. 
            The default is 100.

        Returns
        -------
        None.

        '''

        self.size = size
        self.population = []
        self.exampleMember = exampleMember.copy()
        
        
    def initPopulation(self):
        # Create a population
        self.population = []
        for i in range(self.size):
            member = self.exampleMember.copy()
            member.initialize()
            self.population.append(member)
            
    def getPopulation(self):
        '''
        Get population

        Returns
        -------
        list
            DESCRIPTION. List of members

        '''
        return self.population
    
    def setPopulation(self, population):
        '''
        Set population

        Parameters
        ----------
        population : list
            DESCRIPTION. List of new members

        Returns
        -------
        None.

        '''
        self.population = population
    
