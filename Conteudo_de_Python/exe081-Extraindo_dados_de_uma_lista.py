lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    choice = str(input('Você quer continuar? [s/n]: ')).lower().strip()[0]

    if choice in 'n':
        break
lista.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
print(f'O valor 5 está na lista' if 5 in lista else 'O valor 5 não está na lista')