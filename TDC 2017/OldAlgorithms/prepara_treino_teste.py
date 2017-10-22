# coding=UTF-8

from importar_csv import *
from prepara_tabela import *
from exportar_csv import *
from janelamento import *

import os

#função para separar a tabela em caracteristicas e rotulos
def separa_treino_teste(tabela, tipo):
	x = [] #lista para armazenar as instãncias sem o rotulo
	y = [] #lista para armazenar os rotulos
	#inicia da segunda instância (remove os indices da tabela)
	for i in range(len(tabela)):
		#auxiliar de x
		aux = []
		for j in range(len(tabela[0][:-1])):
			#salva uma instãncia completa sem o rotulo de tamanho n
			aux.append(tabela[i][j])
		#salva auxiliar como um único campo da lista
		x.append(aux)
		#salva apenas o rotulo da instãncia auxiliar
		y.append(tabela[i][-1])
	#verifica se é a mesma tabela para treino e teste
	if (tipo == 'mesma tabela'):
		#verifica a quatidade de instãncias que serão selecionadas para treino
		tamanho = int(len(x)*0.6)
		#treino recebe n instãncias e n rotulos para treinamento
		treino = x[:tamanho], y[:tamanho]
		#teste recebe n instãncias e n rotulos não selecionadas no treino
		teste = x[tamanho:], y[tamanho:]
		#retorna particionado os dados de treino e teste para a mesma tabela
		return (treino, teste)
	#caso o treino e teste seja feito em tabelas diferentes
	else:
		#então retorna apenas a lista x das caracteristicas e y dos rotulos da tabela
		return (x, y)

def prepara_treino_teste(experimento,tabela_treino,tabela_teste,tipo_caracteristica,caracteristica,ponto_articulacao,dados_janelamento,colunas):

	if ((tabela_treino[0] == tabela_teste[0]) and (len(tabela_treino) == 1)):
		tabela_completa = tabela_csv('Data/'+str(tabela_treino[0]))
		tabela = seleciona_caracteristica(tabela_completa, colunas)

		tabela_janelada = janelar_tabela(tabela, dados_janelamento['tamanho_janela'], dados_janelamento['rotulo'])
		tabela = tabela_janelada
		separa = separa_treino_teste(tabela, 'mesma tabela')
		return (separa)