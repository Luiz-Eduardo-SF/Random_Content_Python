
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2

print(f'A média dos valores {n1} e {n2} é {média}')
if média > 7:
    print('O aluno está APROVADO')
elif média < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está de RECUPERAÇÃO')