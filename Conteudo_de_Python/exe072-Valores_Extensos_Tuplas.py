numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)

while True:
    valor = int(input('Digite um valor de 0 a 20: '))
    if 0 <= valor <= 20:
        print(numeros_por_extenso[valor])
        break
    else:
        print('Tente novamente.')