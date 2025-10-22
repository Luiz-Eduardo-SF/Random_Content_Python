# criando uma função que sorteia numeros e armazena em uma lista e outra que le a lista e retorna a soma dos pares
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0,5):
        valor = randint(1,10)
        lista.append(valor)
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!!!')

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    return print(f'Somando os valores pares de {lista}, temos {soma}')

    
valores = list()
sorteia(valores)
somaPar(valores)