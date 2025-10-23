import funcoes

val = float(input('Digite um preço: '))
print(f'A metade de R${val} é R${funcoes.metade(val)}')
print(f'O dobro de R${val} é R${funcoes.dobro(val)}')
print(f'Aumentando 10%, temos R${val + funcoes.tenPer(val)}')