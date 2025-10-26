import funcoes

val = float(input('Digite um preço: '))
print(f'A metade de {funcoes.moeda(val)} é {(funcoes.metade(val, True))}')
print(f'O dobro de {funcoes.moeda(val)} é {(funcoes.dobro(val, coin=True))}')
print(f'Aumentando 10%, temos {(funcoes.aumentar(val, 10, coin=True))}')