num = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

i = 10

while i > 0:
    print(f'{num} →', end=' ')
    num += razão
    i -= 1
print('FIM')