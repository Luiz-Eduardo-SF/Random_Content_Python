color = { # Facilitando o uso de cores nos exercicios!
    'none' : '\033[m',
    'red' : '\033[0;31m',
    'green' : '\033[0;32m',
    'purple' : '\033[0;35m'
         }

print('\n'*3)
print(f'{color['purple']}-={color["none"]}'*30)
print(f'Sistema de Calculo de Emprestimos')
print(f'{color['purple']}-={color["none"]}'*30)

# Pegando os dados

casa = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite seu salário: R$'))
meses = int(input('Quantos anos você vai pagar?: ')) * 12

print(f'{color['purple']}-={color["none"]}'*30)

# Calculando os valores
print(f'A prestação da casa fica no preço de: R${casa / meses:.2f}')

if (casa / meses) > (sal * 0.30):
    print(f'Emprestimo {color['red']}NEGADO!!!{color['none']}') 
else:
    print(f'Emprestimo {color['green']}CONCEDIDO{color['none']}')

print(f'{color['purple']}-={color["none"]}'*30)
