choice = '0'
media = soma = cont = maior = menor = 0
while choice not in 'nN':
    val = int(input('Digite um número: '))
    choice = str(input('Quer continuar? [S/N]: '))
    soma += val
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = val
    elif val > maior:
        maior = val
    elif val < menor:
        menor = val
print(f'Você digitou {cont} números e a média foi de {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
