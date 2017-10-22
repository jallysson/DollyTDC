# coding=UTF-8

import random

class Person(object):

	__WINDOW_LABEL = ['inicio', 'meio', 'fim']

	def __init__(self):

		self.__c = 0.001
		self.__gamma = 0.001
		self.__windowPosition = random.choice(self.__WINDOW_LABEL)
		self.__windowSize = 1

	def CreatePerson(self):

		__person = [
			self.__c,
			self.__gamma,
			self.__windowSize,
			self.__windowPosition
		]

		return __person