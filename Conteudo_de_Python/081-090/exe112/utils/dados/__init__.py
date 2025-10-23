def leiaDinheiro(txt):
    '''
    -> Escreve um input na tela e verifica se é numerico
    :param n1: Valor real
    :return: Valor corrigido
    '''
    válido = False
    while not válido:
        entrada = str(input(txt)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO! \"{entrada}\" não é um preço válido!\033[m')
        else:
            valido = True
            return float(entrada)

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