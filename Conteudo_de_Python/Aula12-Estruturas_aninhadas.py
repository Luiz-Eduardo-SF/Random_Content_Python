nome = str(input('Digite seu nome: ')).lower() # Pega o nome da pessoa e coloca tudo em minusculo

if nome == 'luiz':
    print('Que nome bonito!')
elif nome in ['morgana','helena','apolo']:
    print('Seu nome é \033[1;33mincrível!\033[m')
else:
    print('Seu nome é bem comum.')

print('Tenha um bom dia!')