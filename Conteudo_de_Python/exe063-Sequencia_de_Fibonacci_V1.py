print('-' * 40)
print('Sequência de Fibonacci')
print('-' * 40)
t1 = 0
t2 = 1
terms = int(input('Quantos termos você quer mostrar?: '))
print('~~~~' * 10)
print(f'{t1} → {t2} →', end=' ')
while (terms - 2) > 0:
    t3 = t1 + t2
    print(f'{t3} →', end=' ')
    t1 = t2
    t2 = t3
    terms -= 1
print('FIM')
print('~~~~' * 10)
