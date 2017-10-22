# coding=UTF-8

import numpy as np
import matplotlib.pyplot as plt

from GeneticAlgorithm import GeneticAlgorithm

class ProgressGraph(object):

	def __init__(self):

		self.geneticAlgorithm = GeneticAlgorithm()

	def Graph(self, generations, maximum, minimum):

		plt.scatter(generations, maximum, s = np.pi * 15, c = '#222222', alpha=0.5)
		plt.scatter(generations, minimum, s = np.pi * 15, c = '#044343', alpha=0.5)

		plt.title('Progressao do fitness', fontsize = 12, fontweight = 'normal')
		plt.xlabel('Geracoes', fontsize = 12)
		plt.ylabel('Fitness', fontsize = 12)
		plt.legend(['maximo', 'minimo'], 'upper right', fontsize = 12)
		plt.savefig('Result/IC')

		plt.close('all')

	def FitnessProgression(self, population):

		fitness = [self.geneticAlgorithm.FitnessCalculator(person) for person in population]

		return max(fitness), min(fitness)
