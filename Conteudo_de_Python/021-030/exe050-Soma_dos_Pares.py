soma = 0
cont = 0
for i in range(0,6):
    value = int(input('Digite um número: '))
    if value % 2 == 0:
        soma += value
        cont += 1

print(f'Você digitou {cont} números PARES e a soma foi: {soma}')