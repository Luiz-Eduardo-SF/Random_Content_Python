# def factorial(num=1):
#     """
#         -> Retorna o fatorial de um número
#         :param num: Valor que deseja ver o factorial
#         :return: Factorial do valor
#     """
#     f = 1
#     for i in range(num, 0, -1):
#         f *= i
#     return f

def par(num=0):
    """
        -> Retorna um valor booleano verdadeiro se o número for par
        :param num: Valor para checar
        :return: True or False
    """
    if num % 2 == 0:
        return True
    else:
        return False


if par(2):
    print('O valor é par!!')
else:
    print('O valor é impar!!')


# help(par)