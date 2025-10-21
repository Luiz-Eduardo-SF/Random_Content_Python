from random import randint

bot = randint(0,10)
tent = 1

print('Olá, eu sou seu computador!!!\nEu pensei em um número de 0 a 10\nTente adivinhar!!')

player = int(input('Digite o valor: '))

while bot != player:

    if player < bot:
        player = int(input(f'O valor que pensei é maior que {player}: '))
    elif player > bot:
        player = int(input(f'O valor que pensei é menor que {player}: '))
    tent += 1

print(f'Você acertou com {tent} tentativas, Parabéns!!')
