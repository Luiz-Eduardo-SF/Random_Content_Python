valores = []
for i in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))

maior = sorted(valores)[-1] # Armazena o ultimo valor de uma lista crescente em uma variavel
menor = sorted(valores)[0] # Armazena o primeiro // // // // // //  // //
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições',end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições',end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
