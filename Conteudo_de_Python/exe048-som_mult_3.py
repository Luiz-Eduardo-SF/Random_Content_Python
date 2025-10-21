soma = 0
cont = 0

for i in range(1, 501, 2): # Pega os valores impares
    if i % 3 == 0: # verifica se eles são multiplos de 3
        cont += 1 # Adiciona um valor a cada número impar multiplo de 3
        soma += i # Adiciona o valor do número ao total

print(f'A soma de todos os {cont} valores, resulta em: {soma}')
