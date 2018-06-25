# coding=UTF-8

import csv
 
#função para importar tabela em .csv
def tabela_csv(tabela):
	#informar só o nome com extensão caso a tabela esteja no mesmo local do algoritmo. Se não informar diretório completo
    with open(tabela, 'rb') as csvfile: 
    	#ler todas as linhas do arquivo
        linhas = csv.reader(csvfile)
        #faz uma copia das linhas (matriz) do tipo string
        nova_tabela = list(linhas)
        #percorre todas as linhas da matriz
        for x in range(1,len(nova_tabela)):
        	#percorre todas as colunas da matriz até chegar no timestamp
            for y in range(len(nova_tabela[0][:-4])):
            	#converte todos os valores da matriz em float, menos a coluna dos rotulos
                nova_tabela[x][y] = float(nova_tabela[x][y])
                #retorna a tabela pronta para ser usada
        return (nova_tabela)