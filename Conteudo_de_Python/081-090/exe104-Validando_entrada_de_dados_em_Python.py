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

#programa principal 
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')