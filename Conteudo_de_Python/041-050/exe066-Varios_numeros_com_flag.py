soma = cont = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números, e a soma de todos os valores é de {soma}')