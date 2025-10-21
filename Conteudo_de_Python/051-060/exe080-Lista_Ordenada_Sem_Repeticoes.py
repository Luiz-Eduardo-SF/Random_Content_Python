lista = []
for i in range(0,5):
    valor = int(input('digite um valor: '))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if valor < lista[pos]:
                lista.insert(pos, valor)
                print(f'O valor foi adicionado na posição {pos} da lista')
                break
            pos += 1
print('-='*40)
print(lista)
