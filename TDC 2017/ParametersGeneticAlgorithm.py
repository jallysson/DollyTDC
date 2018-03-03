# coding=UTF-8

import sys
sys.path.append("GeneticAlgorithm")

from Main import Main

class Parameters(object):

	def __init__(self):
		self._populationSize = 25
		self._numberGenerations = 100
		self._crossover = 10
		self._mutation = 10
		self._selection = 10

	def Run(self):
		main = Main(self._populationSize, self._numberGenerations, self._crossover, self._mutation, self._selection)
		main.Run()

parameters = Parameters()
parameters.Run()