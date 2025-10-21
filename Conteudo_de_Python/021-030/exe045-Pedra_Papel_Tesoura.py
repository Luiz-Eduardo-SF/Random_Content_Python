from random import randint
from time import sleep

bot = randint(0,2)

print('''Suas Opções
[0] Pedra
[1] Papel
[2] Tesoura''')

player = int(input('Qual é a sua jogada?: '))

if player > 2 or player < 0:
    print('Opção inválida, tente novamente')
    exit()

choice = {
    0 : 'Pedra',
    1 : 'Papel',
    2 : 'Tesoura'
}

print('JO')
sleep(1)
print('KÊN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 20)
print(f'Computador jogou {choice[bot]}')
print(f'Jogado jogou {choice[player]}')
print('-=' * 20)

if player == bot:
    print('EMPATE')
elif player == 0:
    if bot == 2:
        print('Jogador Ganhou!')
    elif bot == 1:
        print('Computador Ganhou!')
elif player == 1:
    if bot == 0:
        print('Jogador Ganhou!')
    elif bot == 2:
        print('Computador Ganhou!')
elif player == 2:
    if bot == 1:
        print('Jogador Ganhou!')
    elif bot == 0:
        print('Computador Ganhou!')
