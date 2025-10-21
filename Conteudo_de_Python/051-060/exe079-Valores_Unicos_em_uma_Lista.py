lista = list()
while True:
    valor = int(input('Digite um valor: '))
    
    if valor in lista:
        print('Valor duplicado! Não vou adicionar....')
    else:
        lista.append(valor)

    choice = str(input('Deseja continuar? [S/N]: ')).strip().lower()

    if choice in 'Nn':
        break
print('-=' * 40)
print(f'Você digitou os valores {sorted(lista)}')