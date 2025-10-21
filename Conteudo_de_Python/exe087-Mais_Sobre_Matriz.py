matriz = [[[],[],[]],[[],[],[]],[[],[],[]]] # Criado ua matriz 3x3
soma = somacol = maior = 0 # declarando umas variaveis com valor de 0
for i, lins in enumerate(matriz): # pegando o index e o valor de cada linha
    for j, cols in enumerate(matriz): # pegando o index e o valor de cada coluna
        matriz[i][j] = (int(input(f'Digite um valor para [{i},{j}]: '))) # Pedindo os valores para o usuário e armazenando nas células
        if matriz[i][j] % 2 == 0: # Se o valor digitado for par
            soma += matriz[i][j] # Aumenta um no valor da soma de valores pares
        if j == 2: # se for a terceira coluna
            somacol += matriz[i][j] # soma os valores digitados da terceira coluna
        if i == 1: # Se for a segunda linha
            if j == 0: # Se o valor digitado for o primeiro 
                maior = matriz[i][j] # maior recebe o valor digitado
            elif matriz[i][j] > maior: # Se o novo valor digitado na segunda linha for maior que o anterior
                maior = matriz[i][j]  # A variável maior vai receber o novo valor digitado
print('-='*40) 
for i, lins in enumerate(matriz): # verifica cada valor pegando o indice e valor da matriz
    for j, cols in enumerate(matriz): # verifica cada coluna
        print(f'[{matriz[i][j]:^5}]', end='') # Escreve os valores das linhas e colunas na tela
    print() # A cada linha já escrita ele reseta  para escrever a próxima
print('-='*40)
print(f'soma par = {soma}') # Escreve a soma dos valores pares
print(f'soma 3ªcol = {somacol}') # Escreve a soma dos valores da terceira coluna
print(f'maior 2ªlinha = {maior}') # Escreve o maior valor da segunda linha