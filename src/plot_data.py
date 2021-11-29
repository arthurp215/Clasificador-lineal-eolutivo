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
Description: Plot data Linear Classifier

Created on Mon Sep 27 14:14:20 2021

@author: luisa
"""

from matplotlib import pyplot as plt
import numpy as np

class PlotData:
    def plot2D(self, X, Y):
        '''
        Plot the calsses of set of tag data

        Parameters
        ----------
        X : DataFrame
            Contain the attributes.
        Y : Pandas series
            Contain a class or tags.

        Returns
        -------
        None.

        '''
        
        colors = ['or','sg','hb','*y']
        className = list(set(Y))
        
        # Plot
        fig, axs = plt.subplots(1)
        
        name = []
        # Plot selected values
        for i in range(len(className)):
            x = X.loc[Y == className[i]].iloc[:,0]
            y = X.loc[Y == className[i]].iloc[:,1]
            axs.plot(x,y,colors[i])
            name.append(className[i])
        
        # Name of axis
        attName = X.columns
        axs.set_xlabel(attName[0])
        axs.set_ylabel(attName[1])
        axs.legend(name)
        
    def plotLine(self, member):
        '''
        Plot the best line

        Parameters
        ----------
        member : Member
            DESCRIPTION. Object Member

        Returns
        -------
        None.

        '''
        # Intercept
        x = member.getPhenotype()
        b = - x[0] / x[2]
        # Pending
        m = - x[1] / x[2] 
        
        x = np.arange(0, 10, 0.1)
        plt.plot(x, x*m + b) # Plot
        
