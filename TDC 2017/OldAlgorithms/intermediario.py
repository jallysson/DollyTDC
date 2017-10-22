# coding=UTF-8

#importando os outros arquivos que complementam o código 
from est_um_contra_todos import *
from datetime import datetime
from matriz_confusao import *
from gera_arquivo import *
import numpy as np
import os

def intermediario(experimento,estrategia,parametros_svm,dados,dados_treino_teste,dados_janelamento,contador):

	if (estrategia == 'um contra todos'):

		resultado = um_contra_todos(experimento,contador, dados, parametros_svm)

	treino = dados[0]

	teste = dados[1]

	matriz_mc = np.array(resultado[0])

	saidas_svm = np.array(resultado[4])

	matriz_confusao_mc = matriz_mc

	medidas_mc = resultado[1]

	precisao_mc = medidas_mc[0]

	revocacao_mc = medidas_mc[1]

	f_score_mc = medidas_mc[2]

	dados_arquivo = {

		'matriz_confusao_mc': matriz_confusao_mc,

		'precisao_mc': precisao_mc,

		'revocacao_mc': revocacao_mc,

		'f_score_mc': f_score_mc,
	}

	return (dados_arquivo)