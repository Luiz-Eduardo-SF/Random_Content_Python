pares = ''
valores = (
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: '))
)
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro valor 3 está na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

for i in valores:
    if i % 2 == 0:
        pares += str(i) + ' '

if pares == '':
    print('Você não digitou nenhum numero par')
else:
    print(f'Os valores pares digitados foram {pares}')