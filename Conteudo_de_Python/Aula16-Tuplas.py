# lanches = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# # Tuplas são imutáveis
# 
# for i in lanches:
#     print(i)
# 
# for j in range(0, len(lanches)):
#     print(j)
# 
# for pos, comida in enumerate(lanches):
#     print(f'Eu vou comer {comida} na posição {pos}')
# 
# print(sorted(lanches)) # ordena as tuplas

# a = (2, 3, 5)
# b = 6, 9, 10
# c = a+b
# d = b+a
# 
# print(f'{c} é diferente de {d}')


pessoa = ('Gustavo', 39, 'M', 99.88) # As tuplas podem armazenar diversos tipos de valores
del(pessoa) # tuplas podem ser apagadas por completo, mas não é possível apagar somente um item

print(pessoa)