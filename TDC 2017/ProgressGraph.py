# coding=UTF-8

import numpy as np
import operator
import matplotlib.pyplot as plt

from GeneticAlgorithm import GeneticAlgorithm

class ProgressGraph(object):

	def __init__(self):

		self.geneticAlgorithm = GeneticAlgorithm()

	def Graph(self, generations, maximum, minimum):
		plt.plot(generations, maximum, ls = '', marker='o', c = '#2EB872', alpha = 0.5)
		plt.plot(generations, minimum, ls = '', marker='o', c = '#363333', alpha = 0.5)

		plt.title('Progressao do fitness', fontsize = 12, fontweight = 'normal')
		plt.xlabel('Geracoes', fontsize = 12)
		plt.ylabel('Fitness', fontsize = 12)
		#plt.legend(['maximo', 'minimo'], 'upper right', fontsize = 12)
		plt.savefig('Result/IC.eps')

		plt.close('all')

	def FitnessProgression(self, population):

		fitness = [self.geneticAlgorithm.FitnessCalculator(person) for i, person in enumerate(population)]

		index, value = max(enumerate(fitness), key=operator.itemgetter(1))

		return max(fitness), min(fitness), population[index]
