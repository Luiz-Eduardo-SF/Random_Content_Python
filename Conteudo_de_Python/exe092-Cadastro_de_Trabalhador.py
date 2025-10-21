from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['ano_contr'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano_contr'] + 35) - datetime.now().year)
print('-=' * 40)

for k,v in dados.items():
    print(f'- {k} tem o valor {v}')