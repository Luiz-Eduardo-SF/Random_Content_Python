import utils as ut

val = float(input('Digite um preço: '))
print(f'A metade de R${val} é R${ut.metade(val)}')
print(f'O dobro de R${val} é R${ut.dobro(val)}')
print(f'Aumentando 10%, temos R${val + ut.tenPer(val)}')