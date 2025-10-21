from random import randint
win = 0
print('-=' * 30)
print('Vamos jogar par ou impar')
while True:
    bot = randint(0,10)
    print('-='*30)
    value = int(input('Diga um valor: '))
    choice = str(input('Par ou Ímpar? [P/I]: ')).strip()


    if (value + bot) % 2 == 0:
        print(f'Você jogou {value} e o computador {bot}. Total de {value + bot} Deu Par!')
        
        if choice in 'Pp':
            print('Você Venceu!')
            print('Vamos jogar novamente!...')
            win += 1
        elif choice in 'Ii':
            print('Você perdeu!')
            break

    elif (value + bot) % 2 != 0:
        print(f'Você jogou {value} e o computador {bot}. Total de {value + bot} Deu Impar!')

        if choice in 'Ii':
            print('Você venceu!')
            print('Vamos jogar novamente!...')
            win += 1

        elif choice in 'Pp':
            print('Você perdeu!')
            break
print('-=' * 30)
print(f'GAME OVER! Você venceu {win} vezes!')