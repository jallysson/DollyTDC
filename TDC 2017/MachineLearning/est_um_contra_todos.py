# coding=UTF-8



'''importando outros arquivos de códigos'''

import os

from SVM import *

from medidas_avaliacao import *

from prepara_treino_teste_binario import *

from matriz_confusao import *

from exportar_csv import *



def um_contra_todos(experimento,contador,treino_teste,parametros_svm):

	#lista que define os rotulos existentes

	classes = ['D','P','H','S','R']

	#pega os dados de treino passado por parâmetro

	treino = treino_teste[0]

	#pega os dados de teste passado por parâmeto

	teste = treino_teste[1]

	#pega todos os rotulos dos dados de teste e coloca em uma lista

	classes_teste = teste[-1]

	'''listas auxiliares'''

	verdadeiro = []

	predicao = []

	predicao_decisao = []

	teste_mb = []

	#percorre todos os rotulos da lista classes e cria os modelos para cada rotulo

	for classe in classes:

		#prepara os dados de treino binario de acordo com a classe recebida

		treino_binario = prepara_um_contra_todos(treino, classe)

		#prepara os dados de teste binario de acordo com a classe recebida

		teste_binario = prepara_um_contra_todos(teste, classe)

		#executa a svm com os dados de treino binário e teste binário

		SVM = executa_svm(parametros_svm['kernel'],parametros_svm['c'],parametros_svm['gamma'],treino_binario,teste_binario)

		#recebe os rotulos de predição e as saídas de decisão para todos os dados de teste

		aux_predicao_decisao = SVM[0], SVM[1]

		#adiciona a lista de predições e de saídas da svm dentro de outra lista

		predicao_decisao.append(aux_predicao_decisao)

		#adiciona em uma lista todos os rotulos de teste para cada modelo

		teste_mb.append(teste_binario[1])

	'''depois de todos os modelos criados e feita todas as predições'''

	#recebe a lista de predicao de rotulos e saída de descisão para todos os dados de teste do classificador de descanso

	predicao_decisao_d = predicao_decisao[0]

	#recebe a lista de predicao de rotulos e saída de descisão para todos os dados de teste do classificador de preparação

	predicao_decisao_p = predicao_decisao[1]

	#recebe a lista de predicao de rotulos e saída de descisão para todos os dados de teste do classificador de hold

	predicao_decisao_h = predicao_decisao[2]

	#recebe a lista de predicao de rotulos e saída de descisão para todos os dados de teste do classificador de stroke

	predicao_decisao_s = predicao_decisao[3]

	#recebe a lista de predicao de rotulos e saída de descisão para todos os dados de teste do classificador de retração

	predicao_decisao_r = predicao_decisao[4]

	#recebe a lista de predicao de rotulos para todos os dados de teste do classificador de descanso

	predicao_d = predicao_decisao_d[0]

	#recebe a lista de predicao de rotulos para todos os dados de teste do classificador de preparação

	predicao_p = predicao_decisao_p[0]

	#recebe a lista de predicao de rotulos para todos os dados de teste do classificador de hold

	predicao_h = predicao_decisao_h[0]

	#recebe a lista de predicao de rotulos para todos os dados de teste do classificador de stroke

	predicao_s = predicao_decisao_s[0]

	#recebe a lista de predicao de rotulos para todos os dados de teste do classificador de retração

	predicao_r = predicao_decisao_r[0]

	#recebe a lista de descisão para todos os dados de teste do classificador de descanso

	decisao_d = predicao_decisao_d[1]

	#recebe a lista de descisão para todos os dados de teste do classificador de preparação

	decisao_p = predicao_decisao_p[1]

	#recebe a lista de descisão para todos os dados de teste do classificador de hold

	decisao_h = predicao_decisao_h[1]

	#recebe a lista de descisão para todos os dados de teste do classificador de stroke

	decisao_s = predicao_decisao_s[1]

	#recebe a lista de descisão para todos os dados de teste do classificador de retração

	decisao_r = predicao_decisao_r[1]

	#percorre todos os rotulos dos dados de teste sem ser em binário (normal)

	#salvar saídas e predições dos classificadores em um arquivo csv

	matriz_saidas = []

	labels_matriz_saida = [

		'frame','verdadeiro','classificado',

		'rotulo_d','saida_d',

		'rotulo_p','saida_p',

		'rotulo_h','saida_h',

		'rotulo_s','saida_s',

		'rotulo_r','saida_r'

	]

	matriz_saidas.append(labels_matriz_saida)

	for i, classe in enumerate(teste[-1]):

		temp_matriz_saidas = []

		#lista de possíveis predições

		possivel_predicao = []

		#verifica se o rotulo atual foi classificado como positivo pelo classificador de descanso

		if (predicao_d[i] == 'D'):

			#se o classificador der positivo então salva o rotulo e a saída de decisão da svm

			aux_possivel_predicao = predicao_d[i], decisao_d[i]

			#adiciona a possível predição (rotulo e saída) na lista de possivel predicao

			possivel_predicao.append(aux_possivel_predicao)

		#verifica se o rotulo atual foi classificado como positivo pelo classificador de preparação

		if (predicao_p[i] == 'P'):

			#se o classificador der positivo então salva o rotulo e a saída de decisão da svm

			aux_possivel_predicao = predicao_p[i], decisao_p[i]

			#adiciona a possível predição (rotulo e saída) na lista de possivel predicao

			possivel_predicao.append(aux_possivel_predicao)

		#verifica se o rotulo atual foi classificador como positivo pelo classificado de hold

		if (predicao_h[i] == 'H'):

			#se o classificador der positivo então salva o rotulo e a saída de decisão da svm

			aux_possivel_predicao = predicao_h[i], decisao_h[i]

			#adiciona a possível predição (rotulo e saída) na lista de possivel predicao

			possivel_predicao.append(aux_possivel_predicao)

		#verifica se o rotulo atual foi classificado como positivo pelo classificador de stroke

		if (predicao_s[i] == 'S'):

			#se o classificador der positivo então salva o rotulo e a saída de decisão da svm

			aux_possivel_predicao = predicao_s[i], decisao_s[i]

			#adiciona a possível predição (rotulo e saída) na lista de possivel predicao

			possivel_predicao.append(aux_possivel_predicao)

		#verifica se o rotulo atual foi classificado como positivo pelo classificador de retração

		if (predicao_r[i] == 'R'):

			#se o classificador der positivo então salva o rotulo e a saída de decisão da svm

			aux_possivel_predicao = predicao_r[i], decisao_r[i]

			#adiciona a possível predição (rotulo e saída) na lista de possivel predicao

			possivel_predicao.append(aux_possivel_predicao)

		#verifica se nenhum classificador deu resposta positiva ao frame atual

		if (predicao_d[i]!='D' and predicao_p[i]!='P' and predicao_h[i]!='H' and predicao_s[i]!='S' and predicao_r[i]!='R'):

			aux_possivel_predicao = 'ND', decisao_d[i]

			possivel_predicao.append(aux_possivel_predicao)

			aux_possivel_predicao = 'NP', decisao_p[i]

			possivel_predicao.append(aux_possivel_predicao)

			aux_possivel_predicao = 'NH', decisao_h[i]

			possivel_predicao.append(aux_possivel_predicao)

			aux_possivel_predicao = 'NS', decisao_s[i]

			possivel_predicao.append(aux_possivel_predicao)

			aux_possivel_predicao = 'NR', decisao_r[i]

			possivel_predicao.append(aux_possivel_predicao)

		#percorre a lista de possiveis predições para o dado de teste

		for j, x in enumerate(possivel_predicao):

			#se tiver só um elemento ele já dar como rotulo o classificador que deu positivo

			if (j == 0):

				#salva a primeira saída como a maior

				if (x[0] == 'ND'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

						maior = resto

						classe_predita = 'D'

					if (x[1] < 0.0):

						resto = 0-(x[1])

						maior = resto

						classe_predita = 'D'

				if (x[0]=='D' or x[0]=='P' or x[0]=='H' or x[0]=='S' or x[0]=='R'):

					if (x[1] >= 0.0):

						maior = (x[1])-0

					if (x[1] < 0.0):

						maior = 0-(x[1])

					classe_predita = x[0]

			#se a lista de possivel predicao tiver mais de um elemento e a saída do classificador atual for maior que do anterior

			if (j > 0):

				if (x[0] == 'NP'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

					if (x[1] < 0.0):

						resto = 0-(x[1])

					if (resto < maior):

						maior = resto

						classe_predita = 'P'

				if (x[0] == 'NH'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

					if (x[1] < 0.0):

						resto = 0-(x[1])

					if (resto < maior):

						maior = resto

						classe_predita = 'H'

				if (x[0] == 'NS'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

					if (x[1] < 0.0):

						resto = 0-(x[1])

					if (resto < maior):

						maior = resto

						classe_predita = 'S'

				if (x[0] == 'NR'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

					if (x[1] < 0.0):

						resto = 0-(x[1])

					if (resto < maior):

						maior = resto

						classe_predita = 'R'

				if (x[0]=='D'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

					if (x[1] < 0.0):

						resto = 0-(x[1])

					if (resto > maior):

						maior = resto

						classe_predita = x[0]

				if (x[0]=='P'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

					if (x[1] < 0.0):

						resto = 0-(x[1])

					if (resto > maior):

						maior = resto

						classe_predita = x[0]

				if (x[0]=='H'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

					if (x[1] < 0.0):

						resto = 0-(x[1])

					if (resto > maior):

						maior = resto

						classe_predita = x[0]

				if (x[0]=='S'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

					if (x[1] < 0.0):

						resto = 0-(x[1])

					if (resto > maior):

						maior = resto

						classe_predita = x[0]

				if (x[0]=='R'):

					if (x[1] >= 0.0):

						resto = (x[1])-0

					if (x[1] < 0.0):

						resto = 0-(x[1])

					if (resto > maior):

						maior = resto

						classe_predita = x[0]

		#adiciona todos os rotulos preditos em uma lista dos dados de teste

		predicao.append(classe_predita)

		#-----------------------------------------------------

		temp_matriz_saidas.append(i+1)

		temp_matriz_saidas.append(classe)

		temp_matriz_saidas.append(classe_predita)

		temp_matriz_saidas.append(predicao_d[i])

		temp_matriz_saidas.append(float('%.4f' % decisao_d[i]))

		temp_matriz_saidas.append(predicao_p[i])

		temp_matriz_saidas.append(float('%.4f' % decisao_p[i]))

		temp_matriz_saidas.append(predicao_h[i])

		temp_matriz_saidas.append(float('%.4f' % decisao_h[i]))

		temp_matriz_saidas.append(predicao_s[i])

		temp_matriz_saidas.append(float('%.4f' % decisao_s[i]))

		temp_matriz_saidas.append(predicao_r[i])

		temp_matriz_saidas.append(float('%.4f' % decisao_r[i]))

		matriz_saidas.append(temp_matriz_saidas)

		#-----------------------------------------------------

	# --------------------------------------------------------


	# --------------------------------------------------------

	#salva uma lista de predições com todas as listas de predições de todos os classificadores

	predicao_b = [predicao_d, predicao_p, predicao_h, predicao_s, predicao_r]

	#lista de valores verdadeiros e classificados para os dados de teste multclasse

	verdadeiro_classificado_mc = teste[1], predicao

	#lista de valores verdadeiros e classificados para os dados de teste para cada classificador (binário)

	verdadeiro_classificado_b = teste_mb, predicao_b

	#chama a função de matriz confusão multclasse e passa os dados de verdadeiros e classificados

	matriz_mc = matriz_confusao_multclasse(verdadeiro_classificado_mc)

	#chama a função de matriz confusão binária e passa os dados de verdadeiros e classificados

	matriz_b = matriz_confusao_b(verdadeiro_classificado_b)

	#chama a função de medidas de avaliação e passa a matriz de confusão multclasse

	medidas_mc = medidas_avaliacao_multclasse(matriz_mc)

	#chama a função de medidas de avaliação e passa a matriz de confusão binária

	medidas_b = medidas_avaliacao_b(matriz_b)

	#retorna a matriz de confusão multclasse, medidas de avaliação da multclasse e a matriz confusão binária e as medidas de avaliação da binária

	return (matriz_mc, medidas_mc, matriz_b, medidas_b, matriz_saidas)