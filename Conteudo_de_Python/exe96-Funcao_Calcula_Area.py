# Fazendo uma função que calcula área
def area(larg,alt):
    return print(f'A área de um terreno {larg} x {alt} é de :{larg * alt}m²')
def title(msg):
    print(msg)
    print('-' * len(msg))


# Programa principal
title('Controle de Terrenos')
area(float(input('LARGURA (m): ')) , float(input('Altura (m): ')))
