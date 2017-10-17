# coding=UTF-8

import csv

#função para exportar tabelas no formato csv
def exportar_csv(tabela, diretorio_nome):
	#cria o arquivo csv em branco passando o diretório com o nome do aquivo
	csv_fit = csv.writer(open(diretorio_nome, "wb"))
	#percorre todas as linhas da tabela
	for x in range(len(tabela)):
		#recebe a linha x completa ta tabela
		linha = tabela[x][:]
		#escreve a linha no arquivo csv
		csv_fit.writerow(linha)