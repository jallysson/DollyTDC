# coding=UTF-8

def relatorio_geral(diretorio, dados_parametros, dados_arquivo, medida, classe, time_begin, time_end):
	arquivo = open(diretorio, 'w')
	arquivo.write('------------------------------------------------------------------------------------------------------------------------------\n')
	arquivo.write('Medida de avaliação: '+str(medida)+' - início de execução: '+str(time_begin)+' - fim de execução: '+str(time_end)+'\n')
	arquivo.write('------------------------------------------------------------------------------------------------------------------------------\n')
	arquivo.write('Parametrização do experimento: \n')
	arquivo.write('kernel: '+str(dados_parametros['kernel'])+' - gamma: '+str(dados_parametros['gamma'])+' - c: '+str(dados_parametros['c'])+' - estrategia: '+str(dados_parametros['estrategia'])+'\n')
	arquivo.write('tamanho_janela: '+str(dados_parametros['tamanho_janela'])+' - rotulo: '+str(dados_parametros['rotulo'])+'\n')
	arquivo.write('tabela_treino: '+str(dados_parametros['tabela_treino'])+' - tabela_teste: '+str(dados_parametros['tabela_teste'])+'\n')
	arquivo.write('tipo_caracteristica: '+str(dados_parametros['tipo_caracteristica'])+' - caracteristica'+str(dados_parametros['caracteristica'])+' - ponto_articulacao'+str(dados_parametros['ponto_articulacao'])+'\n')
	arquivo.write('------------------------------------------------------------------------------------------------------------------------------\n')
	arquivo.write('Ordem dos parâmetros das executions: kernel, c, gamma, tipo característica, característica, ponto articulação, tamanho janela, rotulo\n')
	arquivo.write('------------------------------------------------------------------------------------------------------------------------------\n')
	for i, med in enumerate(dados_arquivo):
		if (classe[i] == 'D'):
			outras = 'P,H,S,R'
		if (classe[i] == 'P'):
			outras = 'D,H,S,R'
		if (classe[i] == 'H'):
			outras = 'P,D,S,R'
		if (classe[i] == 'S'):
			outras = 'P,H,D,R'
		if (classe[i] == 'R'):
			outras = 'P,H,S,D'
		arquivo.write('Ordenado pela classe - ('+str(classe[i])+'),'+str(outras)+'\n\n')
		for x in (med):
			arquivo.write(str(x)+'\n\n')
		arquivo.write('------------------------------------------------------------------------------------------------------------------------------\n')
	arquivo.close