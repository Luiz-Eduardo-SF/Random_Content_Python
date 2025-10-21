from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1' : randint(1,6),
    'jogador2' : randint(1,6),
    'jogador3' : randint(1,6),
    'jogador4' : randint(1,6),
}

print('Valores sorteadros:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

# ranking = dict(sorted(jogo.items(), key=lambda item:item[1], reverse=True))
# ou 
ranking = dict(sorted(jogo.items(), key=itemgetter(1), reverse= True))
print('-=' * 40)
print(f'{'LISTA DE GANHADORES':^40}')
for k, v in ranking.items():
    print(f'{k} com o valor {v}')