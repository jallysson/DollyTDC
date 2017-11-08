# coding=UTF-8

import sys
sys.path.append("OldAlgorithms")

from janelamento import janelar_tabela
from ManageData import ManageData

class RectangularWindow(object):

	def __init__(self, windowSize, windowPosition):
		manageData = ManageData()
		self._data = manageData.ImportData('Data/scalar.csv')

		self._windowSize = windowSize
		self._windowPosition = windowPosition

	def DataWindow(self):
		dataWindow = janelar_tabela(self._data, self._windowSize, self._windowPosition)

		return dataWindow

#rectangularWindow = RectangularWindow(2, 'meio')

#print rectangularWindow.DataWindow()