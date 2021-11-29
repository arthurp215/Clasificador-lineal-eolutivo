#!/usr/bin/env python3
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
Description: Test of algorithm Linear Classifier

Created on Wed Oct 13 13:26:29 2021

@author: arturop
"""

from AEvolution import AEvolution
from read_data import ReadData
from plot_data import PlotData
from member import Member
from population import Population
from fitness_function import FitnessFuction
from selection import Selection
import numpy as np

# Read data
read = ReadData()
read.selectData('../data/iris.csv')
read.classificationData()

# Select Attributes
read.showAttributes()
a = int(input('Selecciona un atributo: '))
b = int(input('Selecciona otro atributo: '))

# Select classes
read.showTag()
c = int(input('Selecciona una clase: '))
d = int(input('Selecciona otra clase: '))

# Select the corect dataframe
read.selectDataValues(c - 1, d - 1)

# Plot values an classes
gc = PlotData()
#gc.plot2D(read.getValuesX().iloc[:, [a - 1,b - 1]], read.getTag())

# Create a algorithm 
X = read.getValuesX().iloc[:, [a-1, b-1]]

Y = read.getTag()

example = Member(X.shape[1], list(-1*np.ones(X.shape[1])), list(1*np.ones(X.shape[1])))
example.initialize()
population = Population(example, 5)
population.initPopulation()
ff = FitnessFuction(X, Y)
selection = Selection(ff)
#[0.657989501953125, 0.35418701171875, -0.934967041015625]

ae = AEvolution(population, ff, selection, generations=10)
ae.evole(100)

