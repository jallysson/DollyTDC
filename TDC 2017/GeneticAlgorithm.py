# coding=UTF-8

import sys
sys.path.append("OldAlgorithms")

import random

from Principal import Principal
from CrossoverOnePointOrder import crossover_one_point_order

class GeneticAlgorithm(object):

	fitness = {}

	def __init__(self):
		pass

	def SelectionByClassification(self, population):

		self.__numberOfChildren = 10

		marked = [(self.FitnessCalculator(person), person) for person in population]
		marked = [person[1] for person in sorted(marked)]

		selected = marked[(len(marked) - self.__numberOfChildren):]

		return selected

	def ExchangeOfPopulationForAll(self, selected, population):

		sizePopulation = len(population)
		children = self.__CrossoverOnePoint(selected)

		mutationRate = (len(population) * 3) / 100
		crossoverRate = (len(population) * 30) / 100

		for x in range(crossoverRate):

			marked = [(self.FitnessCalculator(son), son) for son in children]
			marked = [son[1] for son in sorted(marked)]
			population.append(marked[-1])

		for x in range(mutationRate):

			population = self.__RandomMutation(population)

		test = [person for person in sorted(population)]

		return test[len(population) - sizePopulation:]

	def __CrossoverOnePoint(self, selected):

		parents = random.sample(selected, 2)

		firstFather = parents[0]
		secondFather = parents[1]

		point = random.randint(1, len(firstFather) - 2)

		firstSon = [firstFather[x] for x in range(point)]
		firstSon = firstSon + [secondFather[x] for x in range(point, len(secondFather))]

		secondSon = [secondFather[x] for x in range(point)]
		secondSon = secondSon + [firstFather[x] for x in range(point, len(secondFather))]

		return firstSon, secondSon

	def FitnessCalculator(self, person):
		keys = self.fitness.keys()

		if (str(person) in keys):
			measure = self.fitness[str(person)], person

		else:

			measure = Principal(person[0], person[2], person[4], person[6])
			self.fitness[str(person)] = sum(measure.Fscore())

		return self.fitness[str(person)]

	def __RandomMutation(self, population):

		__WINDOW_LABEL = ['inicio', 'meio', 'fim']
		personId = random.randint(0, len(population) - 1)

		person = population[personId]
		geneId = random.randint(0, len(person) - 1)

		while (person[geneId] == "*"):

			geneId = random.randint(0, len(person) - 1)

		if (type(person[geneId]) is int):

			person[geneId] = random.randint(1, 10)
			population[personId] = person

		if (type(person[geneId]) is float):

			person[geneId] = random.uniform(0, 1)
			population[personId] = person

		if (type(person[geneId]) is str):

			person[geneId] = random.choice(__WINDOW_LABEL)
			population[personId] = person

		return population