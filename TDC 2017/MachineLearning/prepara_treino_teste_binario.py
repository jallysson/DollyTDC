# coding=UTF-8

#função para pegar os rotulos multclasse do treino ou teste e transformar em binário para a classe passada por parâmetro (ex: D e ND)
def prepara_um_contra_todos(dados, classe):
	#lista que vai receber os rotulos
	rotulos = []
	#percorre todas as linhas dos rotulos (na posição [0] tem as caracteristicas, na posição [1] tem os rotulos)
	for i, t in enumerate(dados[1]):
		#t recebe o rotulo da linha da tabela e verifica se é diferente da classe (ou rotulo) para transformar em binário
		if (t != classe):
			#se não for igual recebe NClasse (ex: ND)
			t = 'N'+classe
		#adiciona o rotulo na lista de rotulos
		rotulos.append(t)
	#retorna o treino ou teste sem os rotulos (caracteristicas) e os novos rotulos binários 
	return (dados[0], rotulos)