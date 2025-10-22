from datetime import datetime

def voto():
    print('-' * 30)
    ano = int(input('Em que ano você nasceu?: '))
    idade = datetime.today().year - ano
    if idade < 16:
        return print(f'Com {idade} anos: NÃO VOTA')
    elif 16 <= idade < 18 or idade > 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        return(print(f'Com {idade} anos: VOTO OBRIGATÓRIO'))
    
voto()