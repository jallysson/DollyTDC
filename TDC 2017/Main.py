# coding=UTF-8

import sys
sys.path.append("OldAlgorithms")

from Person import Person
from GeneticAlgorithm import GeneticAlgorithm
from ProgressGraph import ProgressGraph

class Main(object):

	def __init__(self):

		self.__populationSize = 100

		self.__numberGenerations = 50

		self.__progress = []

		geneticAlgorithm = GeneticAlgorithm()

		progressGraph = ProgressGraph()

		population = [ Person().CreatePerson() for person in range(self.__populationSize) ]

		for generation in range(self.__numberGenerations):

			print "----------------------------------"

			print generation, progressGraph.FitnessProgression(population)

			self.__progress.append(progressGraph.FitnessProgression(population))

			selected = geneticAlgorithm.SelectionByClassification(population)

			population = geneticAlgorithm.ExchangeOfPopulationForAll(selected, population)

		maximum = [x[0] for x in self.__progress]
		minimum = [x[1] for x in self.__progress]

		progressGraph.Graph(range(self.__numberGenerations), maximum, minimum)

Main()
		