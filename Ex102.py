def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input(f'Digite um número: '))
print(f'{n}! = {fatorial(n, show=False)}')
