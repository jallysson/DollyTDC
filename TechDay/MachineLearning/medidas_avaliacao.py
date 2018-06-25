# coding=UTF-8

def medidas_avaliacao_multclasse(matriz):
	precisao = []
	revocacao = []
	for linha in range(1, len(matriz)):
		aux_precisao = []
		for coluna in range(1, len(matriz)):
			aux_precisao.append(matriz[coluna][linha])
		precisao.append(aux_precisao)
	for linha in range(1, len(matriz)):
		aux_revocacao = []
		for coluna in range(1, len(matriz)):
			aux_revocacao.append(matriz[linha][coluna])
		revocacao.append(aux_revocacao)

	'''precisão'''

	if(sum(precisao[0]) == 0.0):
		precisao_D = 0.0
	if(sum(precisao[0]) != 0.0):
		precisao_D = matriz[1][1]/sum(precisao[0])

	if(sum(precisao[1]) == 0.0):
		precisao_P = 0.0
	if(sum(precisao[1]) != 0.0):
		precisao_P = matriz[2][2]/sum(precisao[1])

	if(sum(precisao[2]) == 0.0):
		precisao_H = 0.0
	if(sum(precisao[2]) != 0.0):
		precisao_H = matriz[3][3]/sum(precisao[2])

	if(sum(precisao[3]) == 0.0):
		precisao_S = 0.0
	if(sum(precisao[3]) != 0.0):
		precisao_S = matriz[4][4]/sum(precisao[3])

	if(sum(precisao[4]) == 0.0):
		precisao_R = 0.0
	if(sum(precisao[4]) != 0.0):
		precisao_R = matriz[5][5]/sum(precisao[4])

	'''revocação'''

	if(sum(revocacao[0]) == 0.0):
		revocacao_D = 0.0
	if(sum(revocacao[0]) != 0.0):
		revocacao_D = matriz[1][1]/sum(revocacao[0])

	if(sum(revocacao[1]) == 0.0):
		revocacao_P = 0.0
	if(sum(revocacao[1]) != 0.0):
		revocacao_P = matriz[2][2]/sum(revocacao[1])

	if(sum(revocacao[2]) == 0.0):
		revocacao_H = 0.0
	if(sum(revocacao[2]) != 0.0):
		revocacao_H = matriz[3][3]/sum(revocacao[2])

	if(sum(revocacao[3]) == 0.0):
		revocacao_S = 0.0
	if(sum(revocacao[3]) != 0.0):
		revocacao_S = matriz[4][4]/sum(revocacao[3])

	if(sum(revocacao[4]) == 0.0):
		revocacao_R = 0.0
	if(sum(revocacao[4]) != 0.0):
		revocacao_R = matriz[5][5]/sum(revocacao[4])

	'''f-score'''

	if((precisao_D + revocacao_D) == 0.0):
		f_score_D = 0.0
	if((precisao_D + revocacao_D) != 0.0):
		f_score_D = (2.0 * (precisao_D * revocacao_D))/(precisao_D + revocacao_D)

	if((precisao_P + revocacao_P) == 0.0):
		f_score_P = 0.0
	if((precisao_P+revocacao_P) != 0.0):
		f_score_P = (2.0 * (precisao_P * revocacao_P))/(precisao_P + revocacao_P)

	if((precisao_H + revocacao_H) == 0.0):
		f_score_H = 0.0
	if((precisao_H + revocacao_H) != 0.0):
		f_score_H = (2.0 * (precisao_H * revocacao_H))/(precisao_H + revocacao_H)

	if((precisao_S + revocacao_S) == 0.0):
		f_score_S = 0.0
	if((precisao_S + revocacao_S) != 0.0):
		f_score_S = (2.0 * (precisao_S * revocacao_S))/(precisao_S + revocacao_S)

	if((precisao_R + revocacao_R) == 0.0):
		f_score_R = 0.0
	if((precisao_R + revocacao_R) != 0.0):
		f_score_R = (2.0 * (precisao_R * revocacao_R))/(precisao_R + revocacao_R)

	precisao_D = precisao_D * 100
	precisao_P = precisao_P * 100
	precisao_H = precisao_H * 100
	precisao_S = precisao_S * 100
	precisao_R = precisao_R * 100

	revocacao_D = revocacao_D * 100
	revocacao_P = revocacao_P * 100
	revocacao_H = revocacao_H * 100
	revocacao_S = revocacao_S * 100
	revocacao_R = revocacao_R * 100

	'''reduz o resultado para três casas decimais (precisão, revocação e f-score)'''

	lista_precisao = [
		float('%.3f' % precisao_D),
		float('%.3f' % precisao_P),
		float('%.3f' % precisao_H),
		float('%.3f' % precisao_S),
		float('%.3f' % precisao_R)
	]

	lista_revocacao = [
		float('%.3f' % revocacao_D),
		float('%.3f' % revocacao_P),
		float('%.3f' % revocacao_H),
		float('%.3f' % revocacao_S),
		float('%.3f' % revocacao_R)
	]

	lista_f_score = [
		float('%.3f' % f_score_D),
		float('%.3f' % f_score_P),
		float('%.3f' % f_score_H),
		float('%.3f' % f_score_S),
		float('%.3f' % f_score_R)
	]

	return (lista_precisao, lista_revocacao, lista_f_score)

def medidas_avaliacao_b(matrizes):
	lista_precisao = []
	lista_revocacao = []
	lista_f_score = []

	for i, matriz in enumerate(matrizes):
		if(matriz[1][1] + matriz[2][1] == 0.0):
			precisao = 0.0
		if(matriz[1][1]+matriz[2][1] != 0.0):
			precisao = matriz[1][1] / (matriz[1][1] + matriz[2][1])

		if(matriz[1][1] + matriz[1][2] == 0.0):
			revocacao = 0.0
		if(matriz[1][1] + matriz[1][2] != 0.0):
			revocacao = matriz[1][1] / (matriz[1][1] + matriz[1][2])

		if(precisao + revocacao == 0.0):
			f_score = 0.0
		if(precisao + revocacao != 0.0):
			f_score = (2 * (precisao * revocacao)) / (precisao + revocacao)

		precisao = precisao * 100
		revocacao = revocacao * 100

		lista_precisao.append(float('%.3f' % precisao))
		lista_revocacao.append(float('%.3f' % revocacao))
		lista_f_score.append(float('%.3f' % f_score))
	return (lista_precisao, lista_revocacao, lista_f_score)