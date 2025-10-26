from time import sleep
c = ['\033[m',          #0 - sem cores
     '\033[0;31m',   #1 - vermelho
     '\033[0;32m',   #2 - verde
     '\033[0;33m',   #3 - amarelo
     '\033[0;34m',   #4 - azul
     '\033[0;35m',   #5 - Roxo
     '\033[1;30m'    #6 - branco
]

def pyHelp(f):
    title(f'ACESSSANDO O MANUAL DO \'{f}\'', 4)
    sleep(1)
    print(c[3], end='')
    help(f)
    print(c[0], end='')


def title(txt='< Titulo em branco >', cor=0):
    print(c[cor], end='')
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    title('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.lower().strip() in ['sair', 'fim']:
        break
    else:
        pyHelp(comando)
title('ATÉ LOGO', 1)