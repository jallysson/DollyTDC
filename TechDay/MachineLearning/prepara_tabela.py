# coding=UTF-8

from importar_csv import *

#função para selecionar as caracteristicas (colunas da tabela original), de acordo com os indices das colunas passado por parenteses
def seleciona_caracteristica(tabela, colunas):
	#nova tabela só com as caracteristicas desejadas
	tabela_caracteristicas = []
	#percorre todas as linhas tabela
	for x in range(len(tabela)):
		#lista que vai receber uma linha completa da tabela
		linha = []
		#percorre todas as colunas desejadas
		for i, coluna in enumerate(colunas):
			elemento = tabela[x][coluna]
			if (elemento == 'Rest'):
				elemento = 'D'
			if (elemento == 'Preparation'):
				elemento = 'P'
			if (elemento == 'Hold'):
				elemento = 'H'
			if (elemento == 'Stroke'):
				elemento = 'S'
			if (elemento == 'Retraction'):
				elemento = 'R'
			#adiciona o elemento ou rotulo na lista da linha
			linha.append(elemento)
		#adiciona a linha na nova tabela
		tabela_caracteristicas.append(linha)
	#retorna a nova tabela
	return (tabela_caracteristicas)

def combinar_caracteristica(tabelas, colunas):
	todas_tabelas = []
	for i, tabela in enumerate(tabelas):
		temp = seleciona_caracteristica(tabela, colunas)
		todas_tabelas.append(temp)

	juncao = []

	if (len(tabelas) == 2):
		tabela_one = todas_tabelas[0]
		tabela_two = todas_tabelas[1]
		for linha in range(len(tabela_one)):
			juncao.append(tabela_one[linha][:-1]+tabela_two[linha][:])
	if (len(tabelas) == 1):
		tabela_one = todas_tabelas[0]
		for linha in range(len(tabela_one)):
			juncao.append(tabela_one[linha][:])
	return (juncao)