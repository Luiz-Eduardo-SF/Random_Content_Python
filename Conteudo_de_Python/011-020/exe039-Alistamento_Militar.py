from datetime import date
anoNas = int(input('Ano de nascimento: '))
anoAt = date.today().year # - (date.today().year - 2017) FIZ ESSA PARTE PARA COMPARAR AS RESPOSTAS COM O VIDEO DA AULA QUE FOI EM 2017
diferença = anoAt - anoNas

print(f'Quem nasceu em {anoNas} tem {diferença} anos em {anoAt}')

if int(diferença) > 18:
    print(f'Você já deveria ter se alistado há {diferença - 18} anos.')
    print(f'Seu alistamento foi em {anoNas + 18}')
elif int(diferença) == 18:
    print(f'Você deve se alistar esse ano!')
else:
    print(f'Você deverá se alistar no ano de: {anoNas + 18}')

