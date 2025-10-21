while True:
    print('-' * 30)
    tab = int(input('Digite o valor para uma tabuada: '))
    print('-' * 30)
    
    if tab > 0:
        for i in range(1,11):
            print(f'{tab} x {i} = {tab * i}')
    else:
        break    
print('Programa de tabuada encerrada, volte sempre')