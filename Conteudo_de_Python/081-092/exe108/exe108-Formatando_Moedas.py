import funcoes

val = float(input('Digite um preço: '))
print(f'A metade de {funcoes.moeda(val)} é {funcoes.moeda(funcoes.metade(val))}')
print(f'O dobro de {funcoes.moeda(val)} é {funcoes.moeda(funcoes.dobro(val))}')
print(f'Aumentando 10%, temos {funcoes.moeda(funcoes.aumentar(val, 10))}')