color = { # Facilitando o uso de cores nos exercicios!
    'none' : '\033[m',
    'red' : '\033[0;31m',
    'green' : '\033[0;32m',
    'blue' : '\033[0;34m',
    'purple' : '\033[0;35m'
         }

print(f'{color['purple']}-={color['none']}' * 30)
num = int(input('Digite um valor inteiro: '))
print(f'{color['purple']}-={color['none']}' * 30)

print(f'''Para qual tipo de valor você quer converter?{color['blue']}
[1] - BINARIO
[2] - OCTAL
[3] - HEXADECIMAL{color['none']}''')

print(f'{color['purple']}-={color['none']}' * 30)

esc = int(input('Sua opção: '))

print(f'{color['purple']}-={color['none']}' * 30)

if esc == 1:
    print(f'{num} convertido para BINARIO é: {bin(num)[2:]}')
elif esc == 2:
    print(f'{num} convertido para OCTAL é: {oct(num)[2:]}')
elif esc == 3:
    print(f'{num} convertido para HEXADECIMAL é: {hex(num)[2:]}')

else:
    print('Escolha inválida, tente novamente')

print(f'{color['purple']}-={color['none']}' * 30)
