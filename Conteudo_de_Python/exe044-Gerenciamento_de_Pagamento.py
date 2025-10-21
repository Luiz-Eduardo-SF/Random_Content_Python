color = {'blue' : '\033[0;34m', 
         'none' : '\033[m'}

print(f'{color['blue']}-={color['none']}' * 30)
print(f' {' Lojinha do Luiz ':=^59}')

print(f'{color['blue']}-={color['none']}' * 30)
preço = float(input('Digite o preço total das compras?: R$'))
print(f'{color['blue']}-={color['none']}' * 30)


print('''Escolha a forma de pagamento
[1] Dinheiro
[2] Cheque
[3] Cartão à Vista
[4] Cartão Parcelado''')
print(f'{color['blue']}-={color['none']}' * 30)


opção = int(input('Sua escolha: '))
print(f'{color['blue']}-={color['none']}' * 30)


if opção in [1, 2]:
    print('Pagando à vista no dinheiro/cheque, você ganha 10% de desconto!')
    print(f'Pagando assim o valor final de: {preço - (preço * 0.1)}')
elif opção == 3:
    print('Pagando à vista no cartão, você ganha 5% de desconto!')
    print(f'Pagando assim o valor final de: {preço - (preço * 0.05)} ')
elif opção == 4:
    parc = int(input('Em quantas parcelas você quer pagar? (3x ou mais tem 20% de juros): '))
    
    if parc <=2:
        print(f'você vai pagar: {preço}')
    elif parc >2:
        print(f'você vai pagar: {preço + (preço * 0.2)}')

print(f'{color['blue']}-={color['none']}' * 30)

