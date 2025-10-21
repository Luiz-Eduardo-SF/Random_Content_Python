from math import trunc

n1 = float(input("Digite algum valor float: "))
print(f"o valor que você digitou: {n1}\nValor sem casas decimais: {trunc(n1)}")

#ou

print(f"\nO valor que você digitou: {n1}\nValor sem casas decimais: {int(n1)}")

# Isso é bom quando você não precisa repetir diversas vezes, não precisando importar nenhuma biblioteca