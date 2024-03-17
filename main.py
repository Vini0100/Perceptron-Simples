import sys

#Pesos e bias
pesos = [0.0, 0.0]
bias = 0.0

def treinar(operacao, maxIter, txAprend):
    somaErro = 1
    iteracao = 1
    saida = 0.0
    global pesos
    global bias

    while iteracao < maxIter and somaErro > 0:
        somaErro = 0
        for i in range(0, len(operacao)): # uma execução para cada conjunto de entrada
            saida = pesos[0] * operacao[i][0] + pesos[1] * operacao[i][1] + bias  # calcular valor de ativação
            if saida >= 0:
                saida = 1
            else:
                saida=0
            erro = operacao[i][2] - saida #Calculo do erro
            pesos[0] = pesos[0] + txAprend * erro * operacao[i][0]  # ajuste dos pesos
            pesos[1] = pesos[1] + txAprend * erro * operacao[i][1]
            bias = bias + txAprend * erro  # ajuste do bias

            if erro != 0: # acumula quantidade de erros detectados no laço
                somaErro = somaErro + 1

        iteracao += 1  # incrementa o contador de iterações

        if somaErro == 0:# mensagem do resultado do treinamento
            print("Treinamento OK")
        else:
            print("FALHA NO TREINAMENTO...")
            if somaErro == len(operacao):
                print("Falha total no treinamento, nao ha como o sistema realizar este calculo")
                sys.exit()

# inicializar as variaseis necessárias
def testar():
    valor1 = 0
    valor2 = 0
    saida = 0
    operacaoInp = 0
    operacao = 0
    maxIter = 0

    while True: # laço de uso do perceptron
        operacaoInp = int(input("Digite a operação desejada: 1=AND, 2=OR, 3=XOR  - Ou digite um outro valor para sair "))
        if operacaoInp == 1:
            operacao = [[0.0, 0.0, 0.0], # Carregar a matriz de treinamento
                        [0.0, 1.0, 0.0],
                        [1.0, 0.0, 0.0],
                        [1.0, 1.0, 1.0]]
        elif operacaoInp == 2:
            operacao = [[0.0, 0.0, 0.0], # Carregar a matriz de treinamento
                        [0.0, 1.0, 1.0],
                        [1.0, 0.0, 1.0],
                        [1.0, 1.0, 1.0]]
        elif operacaoInp == 3:
            operacao = [[0.0, 0.0, 0.0],  # Carregar a matriz de treinamento
                        [0.0, 1.0, 1.0],
                        [1.0, 0.0, 1.0],
                        [1.0, 1.0, 0.0]]
        else:
            print("O sistema será encerrado")
            sys.exit()
        maxIter = int(input("Defina o máximo de iterações para treinar "))
        txAprend = int(input("Defina a taxa de aprendizado "))
        treinar(operacao, maxIter, txAprend)

        dicisaoWhile = int(input("Deseja continiar com os testes nesta operacao?: 1=Sim, 2=Não "))
        while dicisaoWhile == 1:
            valor1 = int(input("Digite o primeiro valor (0 ou 1): "))
            valor2 = int(input("Digite o segundo valor (0 ou 1): "))
            saida = pesos[0] * valor1 + pesos[1] * valor2 + bias
            if saida >= 0:
                saida = 1
            else:
                saida = 0
            print("Estradas:", valor1, "e", valor2)
            print("Saída: ", saida)
            dicisaoWhile = int(input("Deseja continiar com os testes nesta operacao?: 1=Sim, 2=Não "))
            if dicisaoWhile == 1:
                continue
            else:
                break

# chamada às funções
testar()

