def fatorial(n=1, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param n: Número inteiro.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    print('-' * 30)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c != 1:
                print(f' {c} ', end='x')
            else: 
                print(f' {c} ', end='= ')
    return f


print(fatorial(5, show=False))