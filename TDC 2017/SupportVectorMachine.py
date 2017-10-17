# coding=UTF-8

from sklearn import svm

class SupportVectorMachine(object):

	def __init__(self, kernel, c, gamma, trainingData, dataLabels):

		self.__classifier = svm.SVC(
			kernel = kernel,
			C = c,
			gamma = gamma,
			verbose = False,
			probability = False,
			shrinking = false,
			random_state = None,
			coef0 = 0.0
		)

		self.__trainingData = trainingData
		self.__dataLabels = dataLabels

		self.__classifier.fit(self.__trainingData, self.__dataLabels, sample_weight=None)

	def Decision(self):
		decision = self.__classifier.decision_function(self.__trainingData)

		return decision

	def Predict(self):
		predict = self.__classifier.predict(self.__trainingData)

		return predict
