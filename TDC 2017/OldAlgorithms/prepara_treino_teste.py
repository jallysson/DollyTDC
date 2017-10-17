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
	#verifica se vai ser trenado e testado na mesma tabela
	if ((tabela_treino[0] == tabela_teste[0]) and (len(tabela_treino) == 1)):
		#importa a tabela de treino
		tabela_completa = tabela_csv('Data/'+str(tabela_treino[0]))
		tabela = seleciona_caracteristica(tabela_completa, colunas)

		if not os.path.exists(str(experimento)+'/data/features/'):
			os.makedirs(str(experimento)+'/data/features/')

		exportar_csv(tabela,str(experimento)+'/data/features/'+str(tipo_caracteristica)+'_'+str(caracteristica)+'_'+str(ponto_articulacao)+'.csv')
		if not os.path.exists(str(experimento)+'/data/windows/'):
			os.makedirs(str(experimento)+'/data/windows/')

		tabela_janelada = janelar_tabela(tabela, dados_janelamento['tamanho_janela'], dados_janelamento['rotulo'])
		exportar_csv(tabela_janelada,str(experimento)+'/data/windows/'+str(tipo_caracteristica)+'_'+str(caracteristica)+'_'+str(ponto_articulacao)+'_'+str(dados_janelamento['tamanho_janela'])+'_'+str(dados_janelamento['rotulo'])+'.csv')

		tabela = tabela_janelada
		#recebe já os dados particionado de treino e teste da tabela
		separa = separa_treino_teste(tabela, 'mesma tabela')
		#retorna os dados de treino e teste para uma mesma tabela
		return (separa)
	#caso o treino e teste seja feito em tabelas diferentes
	else:
		cont = 0
		#laço para percorrer todas as strings das tabelas de treino
		for i, x in enumerate(tabela_treino):
			#recebe a tabela de acordo com a string x com nome da tabela de treino
			tabela_completa = tabela_csv('Data/'+x)
			tabela = seleciona_caracteristica(tabela_completa, colunas)

			if not os.path.exists(str(experimento)+'/data/features/'):
				os.makedirs(str(experimento)+'/data/features/')
			exportar_csv(tabela, str(experimento)+'/data/features/'+str(tabela_treino[i]+'_'+str(tipo_caracteristica)+'_'+str(caracteristica)+'_'+str(ponto_articulacao)+'.csv'))

			if not os.path.exists(str(experimento)+'/data/windows/'):
				os.makedirs(str(experimento)+'/data/windows/')

			tabela_janelada = janelar_tabela(tabela, dados_janelamento['tamanho_janela'], dados_janelamento['rotulo'])
			exportar_csv(
				tabela_janelada,
				str(experimento)+'/data/windows/'+str(tabela_treino[i]+'_'+str(tipo_caracteristica)+'_'+str(caracteristica)+'_'+str(ponto_articulacao)+'_'+str(dados_janelamento['tamanho_janela'])+'_'+dados_janelamento['rotulo']+'.csv')
			)
			tabela = tabela_janelada
			#verifica se é a primeira tabela recebida (cont == 0 é um ativador)
			if (cont == 0):
				#recebe a lista x das caracteristicas e a lista y dos rotulos da tabela
				separa = separa_treino_teste(tabela, '')
				#recebe as duas listas separadas para concatenar nas próximas tabelas
				concatena_x = separa[0]
				concatena_y = separa[1]
				#dispara o ativador para continuar com a concatenação
				cont += 1
			#caso não seja mais a primeira tabela de treino
			else:
				#verifica o tamanho da lista concatena para inserir as outras tabelas a partir desse ponto
				size = len(concatena_x)
				#recebe a lista x das caracteristicas e a lista y dos rotulos da tabela
				separa = separa_treino_teste(tabela, '')
				#concatena a tabela junto com as anteriores na lista de caracteristicas
				concatena_x[size:] = separa[0]
				#concatena a tabela junto com as anteriores na lista de rotulos
				concatena_y[size:] = separa[1]
		#treino recebe n instãncias e n rotulos para treinamento 
		treino = concatena_x, concatena_y
		#recebe a tabela de acordo com a string x com nome da tabela de teste
		tabela_completa = tabela_csv('tabelas/'+str(tabela_teste[0]))
		tabela = seleciona_caracteristica(tabela_completa, colunas)

		if not os.path.exists(str(experimento)+'/data/features/'):
				os.makedirs(str(experimento)+'/data/features/')
		exportar_csv(tabela, str(experimento)+'/data/features/'+str(tabela_teste[0]+'_'+str(tipo_caracteristica)+'_'+str(caracteristica)+'_'+str(ponto_articulacao)+'.csv'))

		if not os.path.exists(str(experimento)+'/data/windows/'):
				os.makedirs(str(experimento)+'/data/windows/')

		tabela_janelada = janelar_tabela(tabela, dados_janelamento['tamanho_janela'], dados_janelamento['rotulo'])
		exportar_csv(
			tabela_janelada,
			str(experimento)+'/data/windows/'+str(tabela_teste[0]+'_'+str(tipo_caracteristica)+'_'+str(caracteristica)+'_'+str(ponto_articulacao)+'_'+str(dados_janelamento['tamanho_janela'])+'_'+dados_janelamento['rotulo']+'.csv')
		)
		tabela = tabela_janelada
		#recebe a lista x das caracteristicas e a lista y dos rotulos da tabela de teste
		teste = separa_treino_teste(tabela, '')
		#retorna os dados de treino e teste para diferentes tabelas
		return (treino, teste)