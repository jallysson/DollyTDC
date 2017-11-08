# coding=UTF-8

from sklearn import svm

class SupportVectorMachine(object):

	def __init__(self, kernel, c, gamma, trainingData, dataLabels):

		self._classifier = svm.SVC(
			kernel = kernel,
			C = c,
			gamma = gamma,
			verbose = False,
			probability = False,
			shrinking = false,
			random_state = None,
			coef0 = 0.0
		)

		self._trainingData = trainingData
		self._dataLabels = dataLabels

		self._classifier.fit(self._trainingData, self._dataLabels, sample_weight = None)

	def Decision(self, testData):
		decision = self._classifier.decision_function(testData)

		return decision

	def Predict(self, testData):
		predict = self._classifier.predict(testData)

		return predict
