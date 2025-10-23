import utils as ut

val = float(input('Digite um preço: '))
print(f'A metade de {ut.moeda(val)} é {(ut.metade(val, True))}')
print(f'O dobro de {ut.moeda(val)} é {(ut.dobro(val, coin=True))}')
print(f'Aumentando 10%, temos {(ut.aumentar(val, 10, coin=True))}')