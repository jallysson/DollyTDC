# coding=UTF-8

# importando os outros arquivos que complementam o código 
from intermediario import *
from prepara_tabela import *
from prepara_treino_teste import *
from relatorio_executions import *
from datetime import datetime

class Principal(object):

	def __init__(self, c, gamma, windowSize, windowPosition):

		'''Informações dos dados (parâmetros obrigatórios) '''

		# informar qual o experimento sendo executado para nomear o diretório
		experimento = 'Result'

		# parâmetros de execução do SVM

		# tipo do kernel
		kernel = 'rbf'
		# varia c de 0 a 1000 em intervalos de 50 em 50
		c = [c]
		# abertura da rbf varia de 2^-5 a 2^5 com expoente variando de 1 em 1
		gamma = [gamma]
		# parâmetros de janelamento

		# tamanho da janela
		tamanho_janela = [windowSize]
		# posição do rotulo da janela
		rotulo = [windowPosition]

		'''parâmetros obrigatórios para definir as tabelas de treino e teste'''

		tabela_treino = ['prep_01_001_1_0001_00002_1.csv']
		tabela_teste = ['prep_01_001_1_0001_00002_1.csv']

		'''parâmetro obrigatório para selecionar a estrátegia multiclasse para a svm'''

		# obs: estratégia um contra todos - (ordem dos classificadores) = D, P, H, S, R
		estrategia = 'um contra todos'

		'''parâmetro obrigatórios para selecionar as carcterísticas das tabelas'''

		# colunas da tabela normal (sem janelamento) para selecionar as caracteristicas (-1 siginifica última coluna (rotulo))'''
		colunas = [[0, 1, 2, 3, -1]]

		'''parâmetros que servem apenas para nomear o arquivo txt (recomendo usar para ficar organizado a descrição da execução!!!'''

		# selecionar tipo de caracteristica (escalar ou vetorial: ['escalar'], escalar e vetorial: ['escalar','vetorial'])
		tipo_caracteristica = [['espacial']]

		# label de caracteristica (velocidade ou aceleracao: ['velocidade'], velocidade e aceleracao: ['velocidade','aceleracao']) para nomear o arquivo de saida
		caracteristica = [['xyz']]

		# label de pontos de articulacao (maos ou pulsos: ['maos'], maos e pulsos: ['maos','pulsos']) para nomear arquivo de saida
		ponto_articulacao = [['rh','-1']]

		'''não precisa parâmetrizar a partir daqui!!!'''

		contador = 0

		for i, caracteristicas in enumerate(colunas):
			# pega os parâmetros de treino e teste setados pelo usuário e salva em um dicionário
			dados_treino_teste = {
				'tabela_treino': tabela_treino,
				'tabela_teste': tabela_teste,
				'tipo_caracteristica': tipo_caracteristica[0],
				'caracteristica': caracteristica[0],
				'ponto_articulacao': ponto_articulacao[i]
			}

			for rotulo_posicao in rotulo:
				for janela in tamanho_janela:
					# pega os parâmetros do janelamento setados pelo usuário e salva em um dicionário
					dados_janelamento = {
						'tamanho_janela': janela,
						'rotulo': rotulo_posicao
					}

					dados = prepara_treino_teste(
						experimento,
						dados_treino_teste['tabela_treino'],
						dados_treino_teste['tabela_teste'],
						dados_treino_teste['tipo_caracteristica'],
						dados_treino_teste['caracteristica'],
						dados_treino_teste['ponto_articulacao'],
						dados_janelamento,
						caracteristicas
					)

					for svm_c in c:
						for svm_gamma in gamma:
							# pega os parâmetros da svm setados pelo usuário e salva em um dicionário
							parametros_svm = {
								'kernel': kernel,
								'c': svm_c,
								'gamma': svm_gamma
							}
							contador += 1
							self.__resultado = intermediario(experimento,estrategia,parametros_svm,dados,dados_treino_teste,dados_janelamento,contador)
	def Fscore(self):
		return self.__resultado['f_score_mc']
					