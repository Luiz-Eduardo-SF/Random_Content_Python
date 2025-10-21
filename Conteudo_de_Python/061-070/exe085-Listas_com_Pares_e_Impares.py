num = [[],[]]

for i in range(1,8):
    valor = int(input(f'Digite o {i}º Valor: '))
    if valor % 2 == 0:
        num[0].append(valor) # Armazena os pares na primeira lista da lista composta
    else:
        num[1].append(valor) # Armazena os numeros impares na segunda lista da lista composta
num[0].sort() # Organiza só a primeira lista da lista composta
num[1].sort() # Organiza só a segunda lista da lista composta
print(f'Os valores pares digitados foram: {num[0]}') 
print(f'Os valores impares digitados foram: {num[1]}') 