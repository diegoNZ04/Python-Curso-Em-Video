def metade(x=0, formato=False):
    """
    calcula metade de um valor
    :param x: valor atribuido
    :param formato: (opcional) formata no padrão brasileiro números flutuantes com vírgulas ou padrão americano com ponto
    :return: retorna valor calculado com ou sem a formatação
    """
    resp = x / 2
    return resp if not formato else moeda(resp)


def dobro(x=0, formato=False):
    """
    calcula o dobro de um valor
    :param x: valor atribuido
    :param formato: (opcional) formata no padrão brasileiro números flutuantes com vírgulas ou padrão americano com ponto
    :return: retorna valor calculado com ou sem a formatação
    """
    resp = x * 2
    return resp if not formato else moeda(resp)


def aumentar(x=0, y=0, formato=False):
    """
    calcula aumento de um determinado valor sobre uma porcentagem
    :param x: valor atribuido
    :param y: porcentagem atribuida
    :param formato: (opcional) formata no padrão brasileiro números flutuantes com vírgulas ou padrão americano com ponto
    :return: retorna valor calculado com ou sem a formatação
    """
    resp = ((y / 100) * x) + x
    return resp if formato is False else moeda(resp)


def reduzir(x=0, y=0, formato=False):
    """
    calcula redução de um determinado valor sobre uma porcentagem
    :param x: valor atribuido
    :param y: porcentagem atribuida
    :param formato: (opcional) formata no padrão brasileiro números flutuantes com vírgulas ou padrão americano com ponto
    :return:  retorna valor calculado com ou sem a formatação
    """
    resp = x - ((y / 100) * x)
    return resp if formato is False else moeda(resp)


def moeda(preco=0, moeda='R$'):
    """
    Realiza a formatação de valores monetários dentro dos padrões brasileiros ou internacionais
    :param preco: valor monetário atribuído
    :param moeda: tipo da moeda, ex R$ ou U$ (R$ como padrão)
    :return: retorna a formatação especificada
    """
    return f'{moeda}{preco:>.2f}'.replace('.', ',')