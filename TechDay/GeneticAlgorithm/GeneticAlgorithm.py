# coding=UTF-8

import sys
sys.path.append("MachineLearning")

import random

from Principal import Principal
from CrossoverOnePointOrder import crossover_one_point_order

class GeneticAlgorithm(object):

	_fitness = {}

	_PERSON_INDEX = 1
	_NUMBER_OF_PARENTS = 2
	_FIRST = 0
	_SECOND = 1

	_REST = 0
	_PREPARATION = 1
	_HOLD = 2
	_STROKE = 3
	_RETRACTION = 4

	_C = 0
	_GAMMA = 1
	_WINDOW_SIZE = 2
	_WINDOW_POSITION = 3

	def __init__(self):
		pass

	def SelectionByClassification(self, selection, population):

		marked = [(self.FitnessCalculator(person), person) for person in population]

		#print marked

		marked = [person[self._PERSON_INDEX] for person in sorted(marked)]

		selected = marked[(len(marked) - selection):]

		#print selected

		#print '--------------------------------------'

		return selected

	def ExchangeOfBest(self, children, population):

		sizePopulation = len(population)

		for son in children:
			population.append(son[self._PERSON_INDEX])

		population = [person for person in sorted(population)]

		return population[len(population) - sizePopulation:]

	def CrossoverOnePoint(self, selected):

		parents = random.sample(selected, self._NUMBER_OF_PARENTS)

		firstFather = parents[self._FIRST]

		#print 'Pai 1: ' + str(firstFather)

		secondFather = parents[self._SECOND]

		#print 'Pai 2: ' + str(secondFather)

		point = random.randint(1, len(firstFather) - 2)

		#print 'Point: ' + str(point)

		firstSon = [firstFather[x] for x in range(point)]
		firstSon = firstSon + [secondFather[x] for x in range(point, len(secondFather))]

		secondSon = [secondFather[x] for x in range(point)]
		secondSon = secondSon + [firstFather[x] for x in range(point, len(secondFather))]

		#print 'Filho 1: ' + str(firstSon)

		#print 'Filho 2: ' + str(secondSon)

		#print '----------------------------------------------'

		return firstSon, secondSon

	def FitnessCalculator(self, person):
		keys = self._fitness.keys()

		if (str(person) in keys):
			measure = self._fitness[str(person)], person
		else:

			measure = Principal(person[self._C], person[self._GAMMA], person[self._WINDOW_SIZE], person[self._WINDOW_POSITION])

			measure = measure.Fscore()

			self._fitness[str(person)] = sum(measure)

		return self._fitness[str(person)]

	def RandomMutation(self, population):

		WINDOW_LABEL = ['inicio', 'meio', 'fim']

		personId = random.randint(0, len(population) - 1)

		person = population[personId]

		#print 'Sem mutação: ' + str(person)

		geneId = random.randint(0, len(person) - 1)

		if (type(person[geneId]) is int):

			person[geneId] = random.randint(1, 30)
			population[personId] = person

		if (type(person[geneId]) is float):

			person[geneId] = random.uniform(0, 1)
			population[personId] = person

		if (type(person[geneId]) is str):

			person[geneId] = random.choice(WINDOW_LABEL)

			population[personId] = person

		#print 'Com mutação: ' + str(person)

		#print '----------------------------------------------'

		return population