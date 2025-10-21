alunos = list()
alun = list()
while True:
    alun.append(str(input('Nome: ')))
    alun.append(float(input('Nota 1: ')))
    alun.append(float(input('Nota 2: ')))
    alunos += [alun[:]]
    alun.clear()
    choice = str(input('Quer continuar? [s/n]: ')).strip()[0]
    if choice in 'Nn':
        break
print('-=' * 50)
print(f'{'No. ':<4} {'NOME':<30} {'MÉDIA':^7}')
print('-' * 50)
for i in range(0,len(alunos)):
    media = (alunos[i][1] + alunos[i][2]) / 2
    print(f'{i:<4} {alunos[i][0]:<30} {media:^7.1f}')
while True:
    print('-' * 50)
    choice = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if choice == 999:
        break
    print(f'Notas de {alunos[choice][0]} são {alunos[choice][1], alunos[choice][2]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')