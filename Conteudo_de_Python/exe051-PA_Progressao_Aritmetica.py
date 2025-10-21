# 10 Termos da PA

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = primeiro + (10 - 1) * razão

for i in range(primeiro, décimo + razão, razão):
    print(i, end=' → ')
print('ACABOU')