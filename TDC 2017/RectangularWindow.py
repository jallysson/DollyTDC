# coding=UTF-8

import sys
sys.path.append("OldAlgorithms")

from janelamento import janelar_tabela
from ManageData import ManageData

class RectangularWindow(object):

    __manageData = ManageData()
    __data = __manageData.ImportData('Data/prep_01_003_2_0001_00002_1.csv')

    def __init__(self, windowSize, windowPosition):
    	self.__windowSize = windowSize
    	self.__windowPosition = windowPosition

    def DataWindow(self):
        dataWindow = janelar_tabela(self.__data, self.__windowSize, self.__windowPosition)

        return dataWindow