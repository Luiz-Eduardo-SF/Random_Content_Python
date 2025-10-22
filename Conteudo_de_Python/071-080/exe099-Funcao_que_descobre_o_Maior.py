# Criando uma função que descobre o maior valor passado como parâmetro
from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2,9,10,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
