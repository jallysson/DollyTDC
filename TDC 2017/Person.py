# coding=UTF-8

import random

class Person(object):

	_WINDOW_LABEL = ['inicio', 'meio', 'fim']

	def __init__(self):
		self._c = 0.001
		self._gamma = 0.001
		self._windowPosition = random.choice(self._WINDOW_LABEL)
		self._windowSize = 1

	def CreatePerson(self):
		_person = [ self._c, self._gamma, self._windowSize, self._windowPosition ]

		return _person

person = Person()

# print 'Cromossomo: ' + str(person.CreatePerson())