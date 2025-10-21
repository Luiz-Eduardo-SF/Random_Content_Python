lista = []; pares = []; impares = []

while True:
    valor = int(input('Digite um número: '))
    lista.append(valor)
    choice = str(input('Quer continuar? [s/n]: ')).strip()[0]
    if choice in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A Lista completa é {lista}')
print(f'A Lista de pares é {pares}')
print(f'A Lista de impares é {impares}')
