# Matriz e analise de dados
matriz = []; pessoa = []; maior = menor = cont = 0
print('-=' * 40)
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(matriz) == 0:
        menor = maior = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]
    matriz.append(pessoa[:])
    pessoa.clear()
    choice = str(input('Quer continuar? [s/n]: ')).strip()[0]
    if choice in 'Nn':
        break
print('-=' * 40)
print(f'Ao todo você cadastrou {len(matriz)} pessoas')
print(f'O maior peso foi de {maior}Kg. Preso de:', end=' ')
for i in matriz:
    if i[1] == maior:
        print(f'[{i[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de:', end=' ')
for i in matriz:
    if i[1] == menor:
        print(f'[{i[0]}]', end=' ')
            