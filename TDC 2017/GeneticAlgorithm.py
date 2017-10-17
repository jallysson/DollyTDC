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

		fitnessAll = []

		self.__numberOfChildren = len(population)/2

		for person in population:

			keys = self.fitness.keys()

			if (str(person) in keys):

				fit = self.fitness[str(person)], person
				fitnessAll.append(fit)

			else:

				fit = self.FitnessCalculator(person), person
				fitnessAll.append(fit)
 
				self.fitness[str(person)] = fit

			marked = [person[1] for person in sorted(fitnessAll)]

		selected = marked[(len(marked) - self.__numberOfChildren):]

		return selected, fitnessAll

	def ExchangeOfPopulationForAll(self, selected, population):

		children = self.__CrossoverOnePoint(selected[0])

		mutationRate = (len(population) * 10) / 100

		for x in range(mutationRate):

			population = self.__RandomMutation(population)

		marked = [(self.FitnessCalculator(son), son) for son in children]

		persons = [x for x in selected[1]]

		marked = [son for son in sorted(marked)]

		persons.append(marked[-1])

		marked = [person[1] for person in sorted(persons)]

		population = marked[1:]

		return population

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

		measure = Principal(person[0], person[2], person[4], person[6])

		return sum(measure.Fscore())

	def __RandomMutation(self, population):

		__WINDOW_LABEL = ['inicio', 'meio', 'fim']
		personId = random.randint(0, len(population))

		person = population[personId]
		geneId = random.randint(0, len(person) - 1)

		while (person[geneId] != "*"):

			geneId = random.randint(0, len(person) - 1)

		if (type(person[geneId]) is int):

			person[geneId] = random.randint(1, 100)
			population[personId] = person

		if (type(person[geneId]) is float):

			person[geneId] = random.uniform(0, 1)
			population[personId] = person

		if (type(person[geneId]) is str):

			person[geneId] = random.choice(self.__WINDOW_LABEL)
			population[personId] = person