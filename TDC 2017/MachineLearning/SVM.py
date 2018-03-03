# coding=UTF-8

#importa o método de svm
from sklearn import svm

#executa o SVM do python com os parâmetros passados
def executa_svm(kernel,c,gamma,treino,teste):
    clf = svm.SVC(
    	kernel=kernel, 
    	C=c,
    	gamma=gamma,
    	verbose=False,
    	probability=False, 
    	shrinking=False,
    	random_state=None,
    	coef0=0.0
        #decision_function_shape='ovr'
    )
    #cria o modelo com base nos dados de treino
    clf.fit(treino[0], treino[1], sample_weight=None)
    #saída da SVM para os dados de teste
    decisao = clf.decision_function(teste[0])
    #predição do modelo para os dados de teste
    predicao = clf.predict(teste[0])
    #retona três listas com as classes preditas pelo modelo, saída da execução para cada instância e os parâmetros usados
    return (predicao, decisao, clf.get_params(deep=True))