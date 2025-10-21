from random import randint

valores = (int(randint(0,10)), int(randint(0,10)), int(randint(0,10)), int(randint(0,10)), int(randint(0,10)))

print(valores)
print(sorted(valores))
print(sorted(valores)[0]) # menor valor
print(sorted(valores)[-1]) # maior valor