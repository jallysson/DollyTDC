# coding=UTF-8

import sys
sys.path.append("OldAlgorithms")

import random

from Principal import Principal
from CrossoverOnePointOrder import crossover_one_point_order

class GeneticAlgorithm(object):

	__fitness = {}

	__PERSON_INDEX = 1
	__NUMBER_OF_PARENTS = 2
	__FIRST = 0
	__SECOND = 1

	__REST = 0
	__PREPARATION = 1
	__HOLD = 2
	__STROKE = 3
	__RETRACTION = 4

	__C = 0
	__GAMMA = 1
	__WINDOW_SIZE = 2
	__WINDOW_POSITION = 3

	def __init__(self):
		pass

	def SelectionByClassification(self, selection, population):

		marked = [(self.FitnessCalculator(person), person) for person in population]
		marked = [person[self.__PERSON_INDEX] for person in sorted(marked)]

		selected = marked[(len(marked) - selection):]

		return selected

	def ExchangeOfBest(self, children, population):

		sizePopulation = len(population)

		for son in children:
			population.append(son[self.__PERSON_INDEX])

		population = [person for person in sorted(population)]

		return population[len(population) - sizePopulation:]

	def CrossoverOnePoint(self, selected):

		parents = random.sample(selected, self.__NUMBER_OF_PARENTS)

		firstFather = parents[self.__FIRST]
		secondFather = parents[self.__SECOND]

		point = random.randint(1, len(firstFather) - 2)

		firstSon = [firstFather[x] for x in range(point)]
		firstSon = firstSon + [secondFather[x] for x in range(point, len(secondFather))]

		secondSon = [secondFather[x] for x in range(point)]
		secondSon = secondSon + [firstFather[x] for x in range(point, len(secondFather))]

		return firstSon, secondSon

	def FitnessCalculator(self, person):
		keys = self.__fitness.keys()

		if (str(person) in keys):
			measure = self.__fitness[str(person)], person

		else:

			measure = Principal(person[self.__C], person[self.__GAMMA], person[self.__WINDOW_SIZE], person[self.__WINDOW_POSITION])

			measure = measure.Fscore()[self.__PREPARATION]

			self.__fitness[str(person)] = measure

		return self.__fitness[str(person)]

	def RandomMutation(self, population):

		WINDOW_LABEL = ['inicio', 'meio', 'fim']

		personId = random.randint(0, len(population) - 1)

		person = population[personId]
		geneId = random.randint(0, len(person) - 1)

		if (type(person[geneId]) is int):

			person[geneId] = random.randint(1, 50)
			population[personId] = person

		if (type(person[geneId]) is float):

			person[geneId] = random.uniform(0, 1)
			population[personId] = person

		if (type(person[geneId]) is str):

			person[geneId] = random.choice(WINDOW_LABEL)
			population[personId] = person

		return population