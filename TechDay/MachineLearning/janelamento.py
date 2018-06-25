# coding=UTF-8
# Jallysson M. Rocha - 2015

# função para janelar (retangular) - o parâmetro rotulo é a posição do rotulo (ex: inicio, meio, fim)
def janelar_tabela(tabela, tamanho_janela, rotulo):
    janelado = []
    classes_janelamento = []
    cont = 1
    instancia = 1
    # percorre todas as linhas das tabelas
    while instancia != len(tabela):
        # pega todos os atributos, menos o rotulo
        caracteristicas = tabela[instancia][:-1]
        # pega o rotulo
        classes = tabela[instancia][-1]
        # pega o primeiro frame para a janela
        if(cont == 1):
            janelamento = caracteristicas
            classes_janelamento.append(classes)
        # adiciona os próximos frames na janela
        if(cont != 1):
            janelamento[int(len(janelamento)):] = caracteristicas
            classes_janelamento.append(tabela[instancia][-1])
        # verifica se a janela já está no tamanho desejado
        if(cont == tamanho_janela):
            # verifica se o rotulo é o do início
            if(rotulo == 'inicio'):
                p = 0
            # verifica se o rotulo é o do meio
            if(rotulo == 'meio'):
                if(tamanho_janela % 2 != 0 or tamanho_janela % 2 == 0):
                    if(tamanho_janela == 1):
                        valor = 0
                    if(tamanho_janela != 1):
                        valor = (tamanho_janela/2)
                p = valor
            # verifica se o rotulo é o do fim
            if(rotulo == 'fim'):
                p = -1
            janelamento[int(len(janelamento)):] = classes_janelamento[p]
            janelado.append(janelamento)
            del classes_janelamento[:] 
        instancia +=1
        if(cont == tamanho_janela):
            instancia = (instancia-tamanho_janela)+1
            cont = 0
        cont = cont+1
    return (janelado)