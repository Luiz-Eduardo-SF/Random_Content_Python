print('\033[1;34m-=\033[m'*30)
print('Digite três valores, e eu vou te dizer se é possível\nformar um triângulo com eles')
print('\033[1;34m-=\033[m'*30)

a1 = float(input('Aresta 1: '))
a2 = float(input('Aresta 2: '))
a3 = float(input('Aresta 3: '))

print('\033[1;34m-=\033[m'*30)

if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Esses valores PODEM formar um triângulo!!')

    if a1 == a2 == a3:
        print('Esse triângulo é Equilátero')
    elif a1 != a2 != a3 != a1:
        print('Esse triângulo é Escaleno')
    else:
        print('Esse triângulo é Isósceles')
else: 
    print('Esses valores NÃO PODEM formar um triângulo')

print('\033[1;34m-=\033[m'*30)