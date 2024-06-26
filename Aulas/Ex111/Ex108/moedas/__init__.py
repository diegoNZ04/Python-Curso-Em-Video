def metade(a = 0):
    m = a / 2
    return m


def dobro(a = 0):
    d = a * 2
    return d


def aumentar(a = 0, b = 0):
    au = ((b / 100) * a) + a
    return au


def reduzir(a=0, b=0):
    red = a - ((b / 100) * a)
    return red


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')