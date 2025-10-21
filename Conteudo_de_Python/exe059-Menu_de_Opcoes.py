n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
choice = 0

while choice != 5:
    print('''
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair                    
''')
    choice = int(input('>> Qual é a sua opção?: '))

    if choice == 1:
        print(f'A some de {n1} e {n2} é {n1 + n2}')
    elif choice == 2:
        print(f'O produto de {n1} e {n2} é {n1 * n2}')
    elif choice == 3:
        if n1 > n2:
            print(f'{n1} é maio que {n2}')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}')
        else:
            print('Os valores são iguais')
    elif choice == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif choice == 5:
        print('Saindo do programa!')
    else:
        print('Opção inválida')