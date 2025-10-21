# num = [2, 5, 9, 1] # criando uma lista
# num.append(7) # adicionando 7 no final da lista
# num[1] = 4 # alterando o valor do primeiro indice para 4
# num.insert(2, 2) # adicionando o valor 2 no indice 2
# num.sort(reverse = True) # organiza de forma decrescente 
# num.remove(2) # remove o primeiro elemento == 2 (não remove todos)
# print(num) # mostra a lista no terminal 
# print(f'Essa lista tem {len(num)} elementos') # escreve quantos elementos tem na lista

a = ['Luiz', 'Morgana', 'Mariana']
# b = a # Quando escrita dessa forma, acabamos linkando as listas, e não criando uma cópia
b = a[:] # Essa é a forma correta de criar cópia de listas no python, pois assim pegamos todos os valores da lista a e passamos um por um para a lista b
b[1] = 'Amor da minha vida'
print(f'Lista A: {a}')
print(f'Lista B: {b}')