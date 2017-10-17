# coding=UTF-8

import csv

class ManageData(object):

	__secondLine = 1
	__firstColumn = 0
	__lastNumberField = -4

	def ImportData(self, data):

		with open(data, 'rb') as csvfile:

			lines = csv.reader(csvfile)
			data = list(lines)

    		for line in range(self.__secondLine, len(data)):

    			for column in range(len(data[self.__firstColumn][:self.__lastNumberField])):

    				data[line][column] = float(data[line][column])

    		return data