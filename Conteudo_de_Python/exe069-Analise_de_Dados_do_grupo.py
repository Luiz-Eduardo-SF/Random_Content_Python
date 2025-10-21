maior = mulheres = homens = 0
while True:
    print('-' * 40)
    print(f'{'CADASTRE UMA PESSOA':^40}')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    print('-' * 40)
    choice = str(input('Quer continuar? [S/N]: ')).strip().lower()

    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    elif idade < 20 and sexo in 'Ff':
        mulheres += 1
    if choice in 'Nn':
        break

print('-' * 40)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')