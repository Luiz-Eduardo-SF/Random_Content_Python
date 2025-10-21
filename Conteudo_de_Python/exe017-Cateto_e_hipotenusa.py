from math import hypot

cO = int(input("Digite o valor do primeiro cateto: "))
cA = int(input("Digite o valor do segundo cateto: "))

print(f"A hipotenusa, nessa situação, vai ter o valor de: {hypot(cA,cO):.2f}")