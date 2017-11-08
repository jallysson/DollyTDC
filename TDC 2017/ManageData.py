# coding=UTF-8

import csv

class ManageData(object):

	def __init__(self):
		self._secondLine = 1
		self._firstColumn = 0
		self._lastNumberField = -4

	def ImportData(self, data):
		with open(data, 'rb') as csvfile:
			lines = csv.reader(csvfile)
			data = list(lines)

    		for line in range(self._secondLine, len(data)):
    			for column in range(len(data[self._firstColumn][:self._lastNumberField])):
    				data[line][column] = float(data[line][column])

    		return data