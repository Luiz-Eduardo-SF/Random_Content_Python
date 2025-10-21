expre = str(input('Digite a expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')

# O código a cima foi o que o guanabara fez, ele ensinou como usar um método de pilha para ver se a quantidade de parenteses foi igual

# já no meu código abaixo eu apenas peguei o valor de quantas vezes os parenteses aparece e comparei se foi igual ou não

'''
expressão = str(input('Digite a expressão'))
if expressão.count('(') != expressão.count(')'):
    print('Expressão inválida')
else:
    print('Expressão válida')
'''