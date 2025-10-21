i = cont = soma = 0
while i != 999:
    cont += 1
    soma += i
    i = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma}')