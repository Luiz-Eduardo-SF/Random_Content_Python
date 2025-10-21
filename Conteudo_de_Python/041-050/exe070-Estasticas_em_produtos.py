expensive = times = total = lowerPrice = 0
lowerName = ''
print('-' * 40)
print(f'{'LOJA SUPER BARATÃO':^40}')
print('-' * 40)

while True:
    name = str(input('Nome do produto: ')).strip()
    price = float(input('Preço: R$'))
    choice = str(input('Quer continuar? [s/n]: ')).strip().lower()

    total += price

    if price > 1000:
        expensive += 1
    
    if times == 0 or price < lowerPrice:
        lowerName = name
        lowerPrice = price
        times = 1

    if choice == 'n':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {expensive} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {lowerName} que custa R${lowerPrice:.2f}')
