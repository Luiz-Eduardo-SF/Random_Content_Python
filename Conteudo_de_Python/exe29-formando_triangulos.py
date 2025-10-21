print('\033[1;34m-=\033[m'*30)
print('Digite três valores, e eu vou te dizer se é possível\nformar um triângulo com eles')
print('\033[1;34m-=\033[m'*30)
a1 = float(input('Aresta 1: '))
a2 = float(input('Aresta 2: '))
a3 = float(input('Aresta 3: '))

if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Esses valores PODEM formar um triângulo!!')
else: 
    print('Esses valores NÃO PODEM formar um triângulo')