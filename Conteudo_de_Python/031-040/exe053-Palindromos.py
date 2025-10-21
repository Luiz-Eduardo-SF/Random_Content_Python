# Programa que lê e retorna se é um palindromo ou não
print('-=' * 30)
frase = str(input('Digite uma frase: ')).strip().lower().split()
frase = ''.join(frase)
palindromo = frase[::-1] # Inverte a palavra

'''palindromo = ''

for i in range(len(frase)-1, -1, -1):
    palindromo += str(frase[i])'''

print('-=' * 30)
print(f'A frase fica: {frase}\nE de trás pra frente fica: {palindromo}')

if frase == palindromo:
    print('É um PALINDROMO')
else:
    print('NÃO é um PALINDROMO')

print('-=' * 30)
