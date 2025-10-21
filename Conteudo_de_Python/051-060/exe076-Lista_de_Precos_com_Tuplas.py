lista = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila',120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)
print('=' * 40)
print(f'{'LISTAGEM DE PREÇOS' :^40}')
print('=' * 40)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<31}',end='')
    else:
        print(f'R${lista[i]:>7.2f}')
    
print('=' * 40)