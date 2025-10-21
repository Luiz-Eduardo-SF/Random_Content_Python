lista = []
for i in range(1,6):
    pessoa = float(input(f'Peso da {i}ª pessoa: '))
    lista += [pessoa]

lista.sort()
print(f'O maior peso lido foi de {lista[-1]}Kg')
print(f'O menor peso lido foi de {lista[0]}Kg')