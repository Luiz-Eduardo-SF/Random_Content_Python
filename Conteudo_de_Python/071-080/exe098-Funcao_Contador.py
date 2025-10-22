# Criando uma função que vai receber três parametros e retornar uma Progressão aritmética entre eles
# v1 = inicio v2 = fim v3 = razão
from time import sleep
def pa(v1, v2, v3):
    print('-=' * 30)
    print(f'Contagem de {v1} até {v2} de {v3} em {v3}')
    sleep(2)
    if v3 == 0:
        v3 = 1
    if v1 > v2:
        if v3 > 0:
            v3 *= -1
        v2 -= 1
    else:
        v2 +=1
    for i in range(v1,v2,v3):
        print(f'{i}', end=' ' , flush=True)
        sleep(0.5)
    print('FIM!')

pa(1,10,1)
pa(10,0,2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
pa(int(input('Inicio: ')),int(input('Fim: ')), int(input('Passo: ')))
