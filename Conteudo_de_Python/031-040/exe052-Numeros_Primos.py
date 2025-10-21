color = {'none' : '\033[m',
         'red' : '\033[0;31m',
         'green' : '\033[0;32m',
         'yellow' : '\033[0;33m'}

print(f'{color['green']}-={color['none']}' * 30)
num = int(input('Digite um valor: '))
print(f'{color['green']}-={color['none']}' * 30)

cont = 0

for i in range(1, num + 1):
    if  num % i == 0:
        cont += 1
        print(f'{color['yellow']}{i}',end=' ')
    else:
        print(f'{color['red']}{i}',end=' ')
        
if cont == 2:
    print(f'\n{color['green']}PRIMO')
else:
    print(f'\n{color['red']}NÃO PRIMO') 

print(f'{color['green']}-={color['none']}' * 30)
   