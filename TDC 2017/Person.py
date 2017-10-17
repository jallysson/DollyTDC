# coding=UTF-8

import random

class Person(object):

	__WINDOW_LABEL = ['inicio', 'meio', 'fim']

	def __init__(self):

		self.__c = random.randint(1, 100)
		self.__gamma = random.uniform(0, 1)
		self.__windowPosition = random.choice(self.__WINDOW_LABEL)
		self.__windowSize = random.randint(1, 100)

	def CreatePerson(self):

		__person = [
			self.__c, '*',
			self.__gamma, '*',
			self.__windowSize, '*',
			self.__windowPosition
		]

		return __person