dados = dict()
gols = list()

dados['nome'] = str(input('Nome do jogador: '))
qnt_partidas = int(input(f'Quantas partidas {dados['nome']} jogou?: '))
for i in range(0,qnt_partidas):
    gols.append(int(input(f'   Quantos gols na partida {i + 1}?: ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)

print('-=' * 30)
print(dados)
print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor de {v}')
print('-=' * 30)

print(f'O jogador {dados['nome']} jogou {qnt_partidas} partidas.')
for i in range(0,qnt_partidas):
    print(f'=> Na partida {i+1}, fez {gols[i]} gols.')
print(f'Foi um total de {dados['total']} gols.')
