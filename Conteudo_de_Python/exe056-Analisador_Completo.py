nomeVelho = ''
idadeVelho = 0
médiaIdade = 0
mulheresMenores = 0

print('-=' * 20)


for i in range(1,5):
    print(f'{f' {i}ªPessoa ':=^40}')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    médiaIdade += idade

    if i == 1 and sexo in 'Mm':
        idadeVelho = idade
        nomeVelho = nome
        homem = 1
    elif sexo in 'Mm':
        if idade > idadeVelho:
            idadeVelho = idade
            nomeVelho = nome

    if i == 4:
        médiaIdade = médiaIdade / 4

    if sexo in 'Ff' and idade < 20:
        mulheresMenores += 1

print('-=' * 20)
print(f'A média de idade do grupo é de {médiaIdade}')
print(f'O homem mais velho tem {idadeVelho} anos e se chama {nomeVelho}')
print(f'Ao todo são {mulheresMenores} mulheres com menos de 20 anos')
print('-=' * 20)
