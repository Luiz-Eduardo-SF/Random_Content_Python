import utils as ut

val = float(input('Digite um preço: '))
print(f'A metade de {ut.moeda(val)} é {ut.moeda(ut.metade(val))}')
print(f'O dobro de {ut.moeda(val)} é {ut.moeda(ut.dobro(val))}')
print(f'Aumentando 10%, temos {ut.moeda(ut.aumentar(val, 10))}')