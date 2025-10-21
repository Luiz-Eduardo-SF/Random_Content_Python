from datetime import date
anoNas = int(input('Ano de Nascimento: '))
anoAt = date.today().year
idade = anoAt - anoNas

if idade <= 9:
    print(f'O atleta de {idade} \nÉ um atleta Mirim')
elif idade <= 14:
    print(f'O atleta de {idade} \nÉ um atleta Infantil')
elif idade <= 19:
    print(f'O atleta de {idade} \nÉ um atleta Junior')
elif idade <= 25:
    print(f'O atleta de {idade} \nÉ um atleta Sênior')
else:
    print(f'O atleta de {idade} \nÉ um atleta Master')
