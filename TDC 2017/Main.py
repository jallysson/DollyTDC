# coding=UTF-8

import sys
sys.path.append("OldAlgorithms")

from Parameters import *
from Person import Person
from GeneticAlgorithm import GeneticAlgorithm
from ProgressGraph import ProgressGraph

class Main(object):

	__MAXIMUM_INDEX = 0
	__MINIMUM_INDEX = 1

	def __init__(self):

		self.__progress = []

		population = [ Person().CreatePerson() for person in range(populationSize) ]

		numberMutation = 0

		for generation in range(numberGenerations):

			numberMutation += 1

			if (numberMutation == mutation):

				population = GeneticAlgorithm().RandomMutation(population)

				numberMutation = 0

			print generation, ProgressGraph().FitnessProgression(population)

			self.__progress.append(ProgressGraph().FitnessProgression(population))

			children = []

			for cross in range((len(population) * crossover) / 100):

				children.append(GeneticAlgorithm().CrossoverOnePoint(GeneticAlgorithm().
					SelectionByClassification((len(population) * selection) / 100, population)))

			population = GeneticAlgorithm().ExchangeOfBest(children, population)

		maximum = [fscore[self.__MAXIMUM_INDEX] for fscore in self.__progress]
		minimum = [fscore[self.__MINIMUM_INDEX] for fscore in self.__progress]

		ProgressGraph().Graph(range(numberGenerations), maximum, minimum)
Main()