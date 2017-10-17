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
		time_begin = datetime.now()
		resultado = um_contra_todos(experimento,contador, dados, parametros_svm)
		time_end = datetime.now()

	treino = dados[0]
	teste = dados[1]

	matriz_mc = np.array(resultado[0])
	matriz_b = np.array(resultado[2])

	saidas_svm = np.array(resultado[4])

	matriz_confusao_mc = matriz_mc
	matriz_confusao_b = matriz_b

	matriz_d = matriz_confusao_b[0]
	matriz_p = matriz_confusao_b[1]
	matriz_h = matriz_confusao_b[2]
	matriz_s = matriz_confusao_b[3]
	matriz_r = matriz_confusao_b[4]

	medidas_mc = resultado[1]
	medidas_b = resultado[3]


	precisao_mc = medidas_mc[0]
	revocacao_mc = medidas_mc[1]
	f_score_mc = medidas_mc[2]

	precisao_b = medidas_b[0]
	revocacao_b = medidas_b[1]
	f_score_b = medidas_b[2]

	precisao_d = precisao_b[0]
	precisao_p = precisao_b[1]
	precisao_h = precisao_b[2]
	precisao_s = precisao_b[3]
	precisao_r = precisao_b[4]

	revocacao_d = revocacao_b[0]
	revocacao_p = revocacao_b[1]
	revocacao_h = revocacao_b[2]
	revocacao_s = revocacao_b[3]
	revocacao_r = revocacao_b[4]

	f_score_d = f_score_b[0]
	f_score_p = f_score_b[1]
	f_score_h = f_score_b[2]
	f_score_s = f_score_b[3]
	f_score_r = f_score_b[4]



	dados_arquivo = {
		'estrategia': estrategia,
		'tipo_caracteristica': dados_treino_teste['tipo_caracteristica'],
		'caracteristica': dados_treino_teste['caracteristica'],
		'ponto_articulacao': dados_treino_teste['ponto_articulacao'],
		'kernel': parametros_svm['kernel'],
		'c': parametros_svm['c'],
		'gamma': parametros_svm['gamma'],
		'tabela_treino': dados_treino_teste['tabela_treino'],
		'tabela_teste': dados_treino_teste['tabela_teste'],
		'tamanho_treino': len(treino[0]),
		'tamanho_teste': len(teste[0]),
		'tamanho_janela': dados_janelamento['tamanho_janela'],
		'rotulo': dados_janelamento['rotulo'],
		'matriz_confusao_mc': matriz_confusao_mc,
		'precisao_mc': precisao_mc,
		'revocacao_mc': revocacao_mc,
		'f_score_mc': f_score_mc,
		'matriz_d': matriz_d,
		'matriz_p': matriz_p,
		'matriz_h': matriz_h,
		'matriz_s': matriz_s,
		'matriz_r': matriz_r,
		'precisao_d': precisao_d,
		'precisao_p': precisao_p,
		'precisao_h': precisao_h,
		'precisao_s': precisao_s,
		'precisao_r': precisao_r,
		'revocacao_d': revocacao_d,
		'revocacao_p': revocacao_p,
		'revocacao_h': revocacao_h,
		'revocacao_s': revocacao_s,
		'revocacao_r': revocacao_r,
		'f_score_d': f_score_d,
		'f_score_p': f_score_p,
		'f_score_h': f_score_h,
		'f_score_s': f_score_s,
		'f_score_r': f_score_r,
		'time_begin': time_begin,
		'time_end': time_end,
		'saidas_svm': saidas_svm
	}

	if not os.path.exists(str(experimento)+'/executions/general/'):
		os.makedirs(str(experimento)+'/executions/general/')

	gera_arquivo(str(experimento)+'/executions/general/execution_'+str(contador)+'.txt', dados_arquivo)
	return (dados_arquivo)
