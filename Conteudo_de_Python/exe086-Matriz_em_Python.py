matriz = [
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
]

for i, lins in enumerate(matriz):
    for j, cols in enumerate(matriz):
        matriz[i][j] = (int(input(f'Digite um valor para [{i},{j}]: ')))
print('-='*40)

for i, lins in enumerate(matriz):
    for j, cols in enumerate(matriz):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()