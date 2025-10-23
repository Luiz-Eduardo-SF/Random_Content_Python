def metade(num=0):
    return num / 2

def dobro(num=0):
    return num * 2

def aumentar(num=0, per=0):
    p = num * (per/100)
    return num + p

def moeda(price = 0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.',',')