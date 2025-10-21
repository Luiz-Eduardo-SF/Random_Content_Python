peso = float(input('Qual é o peso? (kg): '))
altura = float(input('Qual é a altura? (m): '))

imc = peso / pow(altura, 2)

if imc < 18.6:
    print(f'O IMC é de {imc:.2f}: Abaixo do peso')
elif imc < 26:
    print(f'O IMC é de {imc:.2f}: Peso ideal')
elif imc < 31:
    print(f'O IMC é de {imc:.2f}: Sobre peso')
elif imc < 41:
    print(f'O IMC é de {imc:.2f}: Obesidade')
else:
    print(f'O IMC é de {imc:.2f}: Obesidade Mórbida \033[0;31mCUIDADO!!!\033[m')