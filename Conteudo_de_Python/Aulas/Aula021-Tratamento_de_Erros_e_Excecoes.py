# um exemplo de tratamento de erro é o seguinte comando
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except (TypeError, ValueError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado')