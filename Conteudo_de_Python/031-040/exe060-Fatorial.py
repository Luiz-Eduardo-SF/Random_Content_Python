# from math import factorial
# fac = factorial(num)

n = int(input('Digite um númeor para\nCalcular seu Fatorial: '))
i = n
f = 1

print(f'O fatorial de {n}! =', end=' ')
while i > 0:
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1
print(f'{f}')