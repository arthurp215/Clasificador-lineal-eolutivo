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
Description: Fitness Function Linear Classifier

Created on Thu Oct  7 17:25:31 2021

@author: KerenMitsue
"""

import numpy as np


def stable_sigmoid( x):
    
        sig = np.where(x < 0, np.exp(x)/(1 + np.exp(x)), 1/(1 + np.exp(-x)))
        return sig    
class FitnessFuction:
    def stable_sigmoid(self, x):
    
        sig = np.where(x < 0, np.exp(x)/(1 + np.exp(x)), 1/(1 + np.exp(-x)))
        return sig    
    def __init__(self, X, Y):
        '''
        Constructor

        Parameters
        ----------
        tag : dataframe
            DESCRIPTION. Classes of data
        values : dataframe
            DESCRIPTION. Values of data

        Returns
        -------
        None.

        '''
        self.tag = Y
        self.values = X
        self.classs = list(set(self.tag))
    

    def fitness(self, member):
        biClass = self.changeClass()
        w = np.array(member.getPhenotype())
        X = self.values.values
        ones = np.ones((X.shape[0], 1))
        X = np.append(ones, X, axis=1)
        ws = np.tile(w, (X.shape[0], 1))
        p = np.sum(X * ws, axis=1)
        p = stable_sigmoid(p)
        Y2 = np.zeros(self.tag.shape[0])
        idx = p >= 0.5
        Y2[idx] = 1
        biClass = np.array(biClass)
        total = np.sum(np.sum(Y2==biClass))
        return total
        
    def fitness2(self, member):
        '''
        Fitness Function

        Parameters
        ----------
        member : Member
            DESCRIPTION. Object Member

        Returns
        -------
        suma : float
            DESCRIPTION. Sum of all the values, dataframe times member

        '''

        biClass = self.changeClass()
        #for i in range (len(self.values)):
        u = np.array(member.getPhenotype())
        v = self.values.values
        i = 0
        suma = 0
        for j in v:
            x = [1]
            x.extend(j.tolist())
            dot = np.dot(u, np.array(x))
            prod = self.stable_sigmoid(dot)
            flag = True
            if prod >= 0.5 and biClass[i] ==1:
                suma += 1#self.stable_sigmoid(dot*1e-3)
                flag = False
            if (prod <= 0.5 and biClass[i] == 0):
                suma += 1#self.stable_sigmoid(dot*1e-3)
                flag = False
            if flag:
                suma -= 1#self.stable_sigmoid(dot*1e-3)
        return suma
        
    def changeClass(self):
        '''
        Change of class all dataframe tag

        Returns
        -------
        biClass : list
            DESCRIPTION. Returns 0 and 1 according to class

        '''
        biClass = []
        for i in self.tag:
            if i == self.classs[0]:
                biClass.append(1)
            else:
                biClass.append(0)        
        return biClass
            
        
            
    