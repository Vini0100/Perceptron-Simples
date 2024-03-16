#Pesos e bias
pesos = [0.0, 0.0]
bias = 0.0

def treinar(operacao):
    somaErro = 1
    iteracao = 1
    maxIter = 1000 # define máximo de iterações para treinar
    saida = 0.0
    txAprend = 1.00 # define a taxa de aprendizado
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

# inicializar as variaseis necessárias
def testar():
    valor1 = 0
    valor2 = 0
    saida = 0
    operacaoInp = 0
    operacao = 0

    while True: # laço de uso do perceptron
        valor1 = int(input("Digite o primeiro valor (0 ou 1): "))
        valor2 = int(input("Digite o segundo valor (0 ou 1): "))
        operacaoInp = int(input("Digite a operação desejada: 1=AND, 2=OR, 3=XOR "))
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
        treinar(operacao)
        saida = pesos[0] * valor1 + pesos[1] * valor2 + bias
        if saida >= 0:
            saida = 1
        else:
            saida = 0
        print("Estradas:", valor1, "e", valor2)
        print("Saída: ", saida)

# chamada às funções
testar()

