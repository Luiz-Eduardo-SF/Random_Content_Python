def moeda(price = 0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.',',')

def metade(num=0, coin=False):
    return num/2 if not coin else moeda(num/2)

def dobro(num=0, coin=False):
    return num*2 if not coin else moeda(num*2)

def aumentar(num=0, per=0, coin=False):
    p = num * (per/100)
    return num + p if not coin else moeda(num + p)

def diminuir(num=0, per=0, coin=False):
    p = num * (per/100)
    return num - p if not coin else moeda(num - p)


def resumo(n1=0,pa=0,pd=0):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço Analisado: \t{moeda(n1)}')
    print(f'Metade do Preço: \t{metade(n1,True)}')
    print(f'Dobro do Preço: \t{dobro(n1,True)}')
    print(f'{pa}% de Aumento: \t{aumentar(n1,pa,True)}')
    print(f'{pd}% de Desconto: \t{diminuir(n1,pd,True)}')
    print('-' * 40)