# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
Inteligencia Artificial
Tema: Algoritmos geneticos
Colaboradores:
    Keren Mitsue Ramírez Vergara
    Luis Arturo Banda Peláez
    Dr. Asdrúbal López Chau
    Descripción: 

Created on Wed Sep 22 15:33:28 2021

@author: luisa
"""

import pandas as pd
import numpy as np

class ReadData:
    def __init__(self):
        '''
        Constructor

        Returns
        -------
        None.

        '''
        self.__data = 0
        self.__attr = 0
        self.__class = 0
        self.__valuesX = 0
        self.__tag = 0
    
    def selectData(self, path):
        '''
        Path of archive

        Parameters
        ----------
        path : str
            DESCRIPTION. Path of archive

        Returns
        -------
        None.

        '''
        self.__data = pd.read_csv(path)      
    
    def showAttributes(self):
        '''
        Show all attributes

        Returns
        -------
        None.

        '''
        print('List of attributes: ')
        for i in range(len(self.__attr) - 1):
            print((i + 1), '.', self.__attr[i])
    
    def showTag(self):
        '''
        Show all Tags

        Returns
        -------
        None.

        '''
        print('List of tags: ')
        for i in range(len(self.__class)):
            print((i + 1), '.', self.__class[i])  
            
    def classificationData(self):
        '''
        Classification of data. 
            In: Classes or tags
                Only values of data values
                List of attributes
                Set of classes

        Returns
        -------
        None.

        '''
        self.__attr = list(self.__data.columns)
        self.__valuesX = self.__data.iloc[:, 0:-1]
        self.__tag = self.__data.iloc[:,-1]
        self.__class = list(set(self.__tag))
        
    def selectDataValues(self, a, b):
        '''
        Select data accordin to selection of tags

        Parameters
        ----------
        a : int
            DESCRIPTION. Position of the selected tag 
        b : int
            DESCRIPTION. Position of the selected tag

        Returns
        -------
        None.

        '''
        # Return true in the identical data
        c = self.__data['class'] == self.__class[a] 
        d = self.__data['class'] == self.__class[b]
        # Select only data where be true
        p1 = np.flatnonzero(c)
        p2 = np.flatnonzero(d)
        # Create new dataframe
        self.__data = pd.concat([self.__data.iloc[p1], self.__data.iloc[p2]])
        # Again classification of data
        self.classificationData()
   
    def maxValue(self):
        '''
        Get a max values of dataframe

        Returns
        -------
        float
            DESCRIPTION. Max number

        '''
        return np.max(self.__valuesX.values)
    
    def getAttributes(self):
        '''
        List of dataframe attributes

        Returns
        -------
        list
            DESCRIPTION. Dataframe attributes

        '''
        return self.__attr

    def getValuesX(self):
        '''
        Get only dataframe values

        Returns
        -------
        dataframe
            DESCRIPTION. Only dataframe values 

        '''
        return self.__valuesX
    
    def getTag(self):
        '''
        Get tags or classes selected for user

        Returns
        -------
        dataframe
            DESCRIPTION. Tags or classes 

        '''
        return self.__tag