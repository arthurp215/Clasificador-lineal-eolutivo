#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Artificial Intelligence
Topic: Genetic Algorithms

authors:
    Keren Mitsue Ramírez Vergara
    Luis Arturo Banda Peláez
    Dr. Asdrúbal López Chau

Description: Member Linear Classifier

Created on Tue Oct  5 00:00:51 2021

"""

import random
import numpy as np
class Member:
    
    def __init__(self, numAttr=2, minValue=None, maxValue=None, nbits=8):
        '''
         
 
         Parameters
         ----------
         numAttr : int, optional
             DESCRIPTION. Number of attributes or variables. The default is 1.
         minValue : list, optional
             DESCRIPTION. Min values for each attribute. The default is None.
         maxValue : TYPE, optional
             DESCRIPTION. Max values for each attribute. The default is None.
         nbits : int, optional
             DESCRIPTION. Number of bits for each variable. The default is 16.
 
         Returns
         -------
         None.
 
         '''
        '''if maxValue is None or minValue is None:
            raise ValueError
        if len(maxValue)!= len(minValue):
            raise ValueError
        if len(maxValue)!=numAttr or len(minValue)!=numAttr:
                raise ValueError
        '''
        self.numAttr = numAttr
        #self.minValue = [np.min(minValue)]
        #self.minValue.extend(minValue)
        self.maxValue = [np.min(maxValue)]
        self.maxValue.extend(maxValue)
        self.minValue = list(-np.array(self.maxValue))
        self.nbits = nbits
        self.delta = [np.abs(self.minValue[k] - self.maxValue[k])/np.power(2., nbits) for k in range(numAttr + 1)]
        self.genes = []
        
    def initialize(self):
        self.genes = []
        for i in range(self.numAttr + 1):
            gen = random.choices([0, 1], k = (self.nbits))
            self.genes.append(gen)
            
    def getGen(self):
        '''
        Get genes

        Returns
        -------
        list
            DESCRIPTION. 

        '''
        return self.genes
    
    def __str__(self):
        return str(self.genes)
    
    def list2String(self, lista):
        return str(lista).replace("[","").replace("]","").replace(",","").replace(" ","")
    
    def toInt(self, lista):
        return int(self.list2String(lista), 2)
    
    def getPhenotype(self):
        '''
        Get phenotype of member

        Returns
        -------
        x : list
            DESCRIPTION. List of real numbers of the gens 

        '''
        phenotype = []
        for i in range(self.numAttr + 1):
            partition = self.toInt(self.genes[i])
            value = self.minValue + self.delta[i] * partition
            phenotype.append(value[0])
        return phenotype
    
    
    def copy(self):
        nuevo = Member(self.numAttr, self.minValue, self.maxValue, self.nbits)
        nuevo.genes = self.genes.copy()
        return nuevo
    
    def getGenotype(self):
        '''
        Get genotype

        Returns
        -------
        list
            DESCRIPTION. List of gens

        '''
        return self.genes
    
    def crossover(self, mother):
        '''
        Crossover between father and mother

        Parameters
        ----------
        mother : Member
            DESCRIPTION. Object Member

        Returns
        -------
        list
            DESCRIPTION. List of sons (Objects Member)

        '''
        #Two points crossover
        mommy = mother.genes
        daddy = self.genes
        sonA = []
        sonB = []
        for i in range(len(mommy)):
            mom = mommy[i].copy()
            dad = daddy[i].copy()
            p13 = int(len(mom) / 3)
            p2 = int(len(mom)) - (2 * p13)
            # Sons are lists
            son1 = dad[0:p13]
            son1.extend(mom[p13:(p2+p13)])
            son1.extend(dad[(p2+p13):])
            son2 = mom[0:(p13)]
            son2.extend(dad[(p13):(p2+p13)])
            son2.extend(mom[(p2+p13):])
            sonA.append(son1)
            sonB.append(son2)
        sonAObj = self.copy()
        sonAObj.genes = sonA
        sonBObj = self.copy()
        sonBObj.genes = sonB
        return [sonAObj, sonBObj]
    
    def mutate(self, bitsToChange=1):
        '''
        Changes bitsToChange in each gene

        Parameters
        ----------
        bitsToChange : int, optional
            DESCRIPTION. Number of bits to change in each gene. 
            The default is 1.

        Returns
        -------
        None.

        '''
        # Elige un índice aleatorio
        for i in range(self.numAttr + 1):
            for nb in range(bitsToChange):
                idx = random.choice(range(self.nbits))
                self.genes[i][idx] = 1 - self.genes[i][idx]