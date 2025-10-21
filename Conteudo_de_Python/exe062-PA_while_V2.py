num = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
term = 0
i = 10

while i > 0:
    print(f'{num} →', end=' ')
    num += razão
    term += 1
    i -= 1

    if i == 0:
        print('PAUSA')
        choice = int(input('Quantos termos a mais você quer?: '))
        
        if choice != 0:
            i += choice
        else:
            print(f'A Progressão foi finalizada com {term} termos mostrados.')
