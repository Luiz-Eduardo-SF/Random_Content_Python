sexo = str(input('Digite seu sexo [M/F]: '))

while sexo not in 'FfMm':
    sexo = str(input('Dado inválido. Por favor, digite seu sexo: '))
print(f'Sexo {sexo} válidado com sucesso!')