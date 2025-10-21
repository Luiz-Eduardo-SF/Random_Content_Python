from datetime import date
maior = 0
menor = 0

print('-=' * 30)

for i in range(1,8):
    pessoa = int(input(f'Em que ano a {i}ª pessoa nasceu?:'))
    if (date.today().year - pessoa) >= 21:
        maior += 1
    else:
        menor += 1

print(f'\nAo todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
print('-=' * 30)