def moeda(price = 0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.',',')

def metade(num=0, coin=False):
    return num/2 if not coin else moeda(num/2)

def dobro(num=0, coin=False):
    return num*2 if not coin else moeda(num*2)

def aumentar(num=0, per=0, coin=False):
    p = num * (per/100)
    return num + p if not coin else moeda(num + p)
