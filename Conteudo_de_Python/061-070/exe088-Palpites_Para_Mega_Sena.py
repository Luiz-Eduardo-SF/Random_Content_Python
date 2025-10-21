from random import randint
from time import sleep
jogos = list()
jogoat = list()

print('-' * 60)
print(f'{'JOGA NA MEGA SENA':^60}')
print('-' * 60)
qnt = int(input('Quantos jogos você quer que eu sorteie?: '))
print(f'{f' SORTEANDO {qnt} JOGOS ' :-^60}')
for i in range(1,qnt+1):
    cont = 0
    while True:
        bot = randint(1,60)
        if bot not in jogoat:
            jogoat.append(bot)
            cont +=1
        if cont >= 6:
            break
    jogoat.sort()
    jogos += [jogoat[:]]
    jogoat.clear()

for i in range(0,qnt):
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(1)
print(f'{f' < BOA SORTE > ' :-^60}')
