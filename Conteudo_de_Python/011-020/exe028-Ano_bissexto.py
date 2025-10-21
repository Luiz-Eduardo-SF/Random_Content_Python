from datetime import date # importa o date da biblioteca datetime

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year # pega o ano atual do sistema

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} NÃO é BISSEXTO')