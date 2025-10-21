a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

# checking the smallest number
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# checking the biggest number
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# printing

print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')