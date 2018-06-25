# coding=UTF-8

import sys
sys.path.append("OldAlgorithms")

from Person import Person
from GeneticAlgorithm import GeneticAlgorithm
from ProgressGraph import ProgressGraph

class Main(object):

	_MAXIMUM_INDEX = 0
	_MINIMUM_INDEX = 1

	def __init__(self, populationSize, numberGenerations, crossover, mutation, selection):
		self._populationSize = populationSize
		self._numberGenerations = numberGenerations
		self._crossover = crossover
		self._mutation = mutation
		self._selection = selection

	def Run(self):
		self._progress = []

		population = [ Person().CreatePerson() for person in range(self._populationSize) ]
		numberMutation = 0

		for generation in range(self._numberGenerations):
			numberMutation += 1

			if (numberMutation == self._mutation):
				population = GeneticAlgorithm().RandomMutation(population)
				numberMutation = 0

			print "Geração " + repr(generation) + " - Melhor solução: ", ProgressGraph().FitnessProgression(population)

			self._progress.append(ProgressGraph().FitnessProgression(population))

			children = []

			for cross in range((len(population) * self._crossover) / 100):
				children.append(GeneticAlgorithm().CrossoverOnePoint(GeneticAlgorithm().
					SelectionByClassification((len(population) * self._selection) / 100, population)))

			population = GeneticAlgorithm().ExchangeOfBest(children, population)

		maximum = [fscore[self._MAXIMUM_INDEX] for fscore in self._progress]
		minimum = [fscore[self._MINIMUM_INDEX] for fscore in self._progress]

		ProgressGraph().Graph(range(self._numberGenerations), maximum, minimum)