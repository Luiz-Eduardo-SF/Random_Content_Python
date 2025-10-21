from random import randint
from time import sleep # pegando o comando sleep da biblioteca time
 
num = randint(0, 5) # Armazena um número aleatório entre 0 e 5
print('-=' * 30)
print('Eu vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=' * 30)
numinp = int(input('Digite um valor: '))
print('PROCESSANDO...')
sleep(3)


if numinp == num:
    print('Parabéns, você acertou o número que eu estava pensando!!')
else:
    print(f'Você errou, o número que eu pensei foi o número: {num}')