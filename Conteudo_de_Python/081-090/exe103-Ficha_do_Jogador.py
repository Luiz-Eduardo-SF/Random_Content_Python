def ficha(nom='<desconhecido>',gol=0):
    """
        -> Apenas uma função para teste
        :param nome: Pega uma string
        :param gols: Pega um valor inteiro
        :return: Uma mensagem com o nome e quantos gols foram feitos
    """
    return print(f'O jogador {nom} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)