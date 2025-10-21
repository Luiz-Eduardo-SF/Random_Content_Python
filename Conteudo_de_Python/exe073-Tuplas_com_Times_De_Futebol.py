times_2025 = (
    "Palmeiras", "Flamengo", "Cruzeiro", "Red Bull Bragantino", "Fluminense",
    "Ceará", "Corinthians", "Vasco da Gama", "Juventude", "São Paulo",
    "Mirassol", "Internacional", "Fortaleza", "Botafogo", "Vitória",
    "Atlético‑MG", "Santos", "Grêmio", "Bahia", "Sport"
)

print(times_2025[0:5])
print(times_2025[-4:])
print(sorted(times_2025))

if 'Chapecoense' in times_2025:
    print(f'A Chapecoense está na posição de nº {times_2025.index('Chapecoense')+1}')
else:
    print('Infelizmente a Chapecoense não faz parte da lista dos 20 primeiros colocados do Brasileirão desse ano(2025).')