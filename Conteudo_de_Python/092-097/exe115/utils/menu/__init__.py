import sys
c= [
    '\033[0;37m',
    '\033[0;31m',
    '\033[0;32m',
    '\033[0;33m',
    '\033[0;34m',
    '\033[0;35m',
    '\033[0;36m',
    '\033[0;30m'
]

def leiaInt(txt):
    ok = False
    valor = 0
    while True: 
        n = str(input(txt))
        
        if n.isnumeric():
            n = int(n)
            valor = n
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok == True:
            break
    return valor

def line(space = 50):
    return '=' * space

def header(txt, space=50):
    print(line())
    print(f'{txt}'.center(space))
    print(line())

def menu(title='SEM TITULO', *num):
    header(title)

    for i in range(0,len(num)):
        print(f'{c[3]}{i+1}{c[0]} - {c[6]}{num[i]}{c[0]}')
    print(f'{c[3]}{len(num)+1}{c[0]} - {c[6]}Sair do sistema{c[0]}')
    
    print(line())

    while True:

        try:
            choice = int(input('Sua opção: '))
            if choice < 1:
                return 1
            if choice == len(num)+1:
                header('Saindo do sistema...')
                return -1
            choice -= 1

            info = num[choice]
            
        except (ValueError , TypeError):
            print(f'{c[1]}ERRO: Por Favor, digite um número inteiro válido!{c[0]}')
        except (IndexError):
            print(f'{c[1]}ERRO: Digite uma opção válida!{c[0]}')
        except (KeyboardInterrupt):
            print(f'{c[1]}\nO usuário escolheu não digitar uma opção!{c[0]}')
            header('Saindo do sistema...')
            return -1
        else:
            return choice + 1