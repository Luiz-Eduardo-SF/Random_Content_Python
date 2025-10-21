# pessoas = {
#     'nome' : 'Luiz',
#     'idade' : 19,
#     'sexo' : 'M'
# }
# 
# for k, v in pessoas.items():
#     print(f'O {k} é {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla' : 'SP'}
brasil.append(estado1.copy())
brasil.append(estado2.copy())

for i in brasil:
    for k, v in i.items():
        print(f'O {k} é {v}')