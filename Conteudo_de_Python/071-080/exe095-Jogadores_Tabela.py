# Programa para cadastrar jogadores, registrar gols por partida e exibir um relatório.
# Estruturas usadas:
# - time: lista de dicionários, cada dicionário representa um jogador
# - jogador: dicionário temporário com chaves 'nome', 'gols' e 'tot'
# - gols: lista temporária de gols por partida

time = list()
jogador = dict()
gols = list()

# Entrada de dados: loop principal para cadastrar vários jogadores
while True:
    jogador.clear()   # limpa dados do dicionário para reutilizar
    gols.clear()      # limpa lista de gols para o próximo jogador

    jogador['nome'] = str(input('Nome do jogador: ')).title()
    jogos = int(input('Quantos jogos ele jogou?: '))

    # coleta gols por partida
    for i in range(0, jogos):
        gols.append(int(input(f'Quantos gols na partida {i+1}?: ')))

    jogador['gols'] = gols[:]     # copia a lista de gols
    jogador['tot'] = sum(gols)   # total de gols
    time.append(jogador.copy())  # adiciona uma cópia do dicionário à lista de jogadores

    choice = str(input('Quer continuar? [s/n]: ')).strip()[0]
    if choice in 'Nn':
        break

# Exibição da tabela resumida de jogadores
print('-=' * 40)
print(f'{"cod.":<4} {"nome":<30} {"gols":<30} {"total":<10}')
print('-' * 80)
for i, v in enumerate(time):
    # mostra índice (código), nome, lista de gols e total
    print(f'{i:>4} {time[i]["nome"]:<30} {time[i]["gols"]:<30} {time[i]["tot"]:<10}')
print('-' * 80)

# Consulta detalhada por jogador
while True:
    data = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if data == 999:
        break
    if data >= len(time) or data < 0:
        print(f'ERRO! Não existe jogador com código {data}')
    else:
        # levantamento detalhado: gols por partida
        print(f' -- LEVANTAMENTO DO JOGADOR {time[data]["nome"]}:')
        for i, v in enumerate(time[data]['gols']):
            print(f'No jogo {i + 1} fez {v} gols.')
print('<< VOLTE SEMPRE >> ')
