# coding=UTF-8

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix

def matriz_confusao_multclasse(verdadeiro_classificado):

	matriz_confusao_multclasse = [
		['','D','P','H','S','R'],
		['D',0.0 , 0.0 , 0.0 , 0.0 , 0.0 ],
		['P',0.0 , 0.0 , 0.0 , 0.0 , 0.0 ],
		['H',0.0 , 0.0 , 0.0 , 0.0 , 0.0 ],
		['S',0.0 , 0.0 , 0.0 , 0.0 , 0.0 ],
		['R',0.0 , 0.0 , 0.0 , 0.0 , 0.0 ]
	]

	verdadeiro = verdadeiro_classificado[0]
	classificado = verdadeiro_classificado[1]

	'''primeira linha'''

	for i in range(len(verdadeiro)):
		if(verdadeiro[i] == 'D' and classificado[i] == 'D'):
			matriz_confusao_multclasse[1][1] += 1.0

		if(verdadeiro[i] == 'D' and classificado[i] == 'P'):
			matriz_confusao_multclasse[1][2] += 1.0

		if(verdadeiro[i] == 'D' and classificado[i] == 'H'):
			matriz_confusao_multclasse[1][3] += 1.0

		if(verdadeiro[i] == 'D' and classificado[i] == 'S'):
			matriz_confusao_multclasse[1][4] += 1.0

		if(verdadeiro[i] == 'D' and classificado[i] == 'R'):
			matriz_confusao_multclasse[1][5] += 1.0

		'''segunda linha'''

		if(verdadeiro[i] == 'P' and classificado[i] == 'D'):
			matriz_confusao_multclasse[2][1] += 1.0

		if(verdadeiro[i] == 'P' and classificado[i] == 'P'):
			matriz_confusao_multclasse[2][2] += 1.0

		if(verdadeiro[i] == 'P' and classificado[i] == 'H'):
			matriz_confusao_multclasse[2][3] += 1.0

		if(verdadeiro[i] == 'P' and classificado[i] == 'S'):
			matriz_confusao_multclasse[2][4] += 1.0

		if(verdadeiro[i] == 'P' and classificado[i] == 'R'):
			matriz_confusao_multclasse[2][5] += 1.0

		'''terceira linha'''

		if(verdadeiro[i] == 'H' and classificado[i] == 'D'):
			matriz_confusao_multclasse[3][1] += 1.0

		if(verdadeiro[i] == 'H' and classificado[i] == 'P'):
			matriz_confusao_multclasse[3][2] += 1.0

		if(verdadeiro[i] == 'H' and classificado[i] == 'H'):
			matriz_confusao_multclasse[3][3] += 1.0

		if(verdadeiro[i] == 'H' and classificado[i] == 'S'):
			matriz_confusao_multclasse[3][4] += 1.0

		if(verdadeiro[i] == 'H' and classificado[i] == 'R'):
			matriz_confusao_multclasse[3][5] += 1.0

		'''quarta linha'''

		if(verdadeiro[i] == 'S' and classificado[i] == 'D'):
			matriz_confusao_multclasse[4][1] += 1.0

		if(verdadeiro[i] == 'S' and classificado[i] == 'P'):
			matriz_confusao_multclasse[4][2] += 1.0

		if(verdadeiro[i] == 'S' and classificado[i] == 'H'):
			matriz_confusao_multclasse[4][3] += 1.0

		if(verdadeiro[i] == 'S' and classificado[i] == 'S'):
			matriz_confusao_multclasse[4][4] += 1.0

		if(verdadeiro[i] == 'S' and classificado[i] == 'R'):
			matriz_confusao_multclasse[4][5] += 1.0

		'''quinta linha'''

		if(verdadeiro[i] == 'R' and classificado[i] == 'D'):
			matriz_confusao_multclasse[5][1] += 1.0

		if(verdadeiro[i] == 'R' and classificado[i] == 'P'):
			matriz_confusao_multclasse[5][2] += 1.0

		if(verdadeiro[i] == 'R' and classificado[i] == 'H'):
			matriz_confusao_multclasse[5][3] += 1.0

		if(verdadeiro[i] == 'R' and classificado[i] == 'S'):
			matriz_confusao_multclasse[5][4] += 1.0

		if(verdadeiro[i] == 'R' and classificado[i] == 'R'):
			matriz_confusao_multclasse[5][5] += 1.0

	return (matriz_confusao_multclasse)

def matriz_confusao_b(verdadeiro_classificado):
	classes = ['D','P','H','S','R']
	aux_classificado = verdadeiro_classificado[1]
	aux_verdadeiro = verdadeiro_classificado[0]
	matrizes_b = []

	for j, classe in enumerate(classes):		
		classificado = aux_classificado[j]
		verdadeiro = aux_verdadeiro[j]
		matriz_confusao_b = [
			['', classe,'N'+str(classe)],
			[classe,0.0,0.0],
			['N'+str(classe),0.0,0.0]
		]
 
		for i in range(len(verdadeiro)):
			if(verdadeiro[i] == classe and classificado[i] == classe):
				matriz_confusao_b[1][1] += 1.0

			if(verdadeiro[i] == classe and classificado[i] == 'N'+str(classe)):
				matriz_confusao_b[1][2] += 1.0

			if(verdadeiro[i] == 'N'+str(classe) and classificado[i] == 'N'+str(classe)):
				matriz_confusao_b[2][2] += 1.0

			if(verdadeiro[i] == 'N'+str(classe) and classificado[i] == classe):
				matriz_confusao_b[2][1] += 1.0

		matrizes_b.append(matriz_confusao_b)

	return (matrizes_b)