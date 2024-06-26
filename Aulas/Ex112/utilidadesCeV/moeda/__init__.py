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


def resumo(x=0, aumento=0, reducao=0):
    """
    mostra o resumo dos do dado preço referente as outras funções do pacote
    :param x: preço atribuido
    :param aumento: porcentagem de aumento atribuida
    :param reducao: porcentagem de redução atribuida
    :return: retorna resumo dos dados com as funcionalidades opcionais
    """
    print('-' * 45)
    print('Resumo do Valor'.center(45))
    print('-' * 45)
    print(f'{"Preço Analisado:":<} \t\t\t\t{moeda(x)}')
    print(f'{"Dobro do Preço:":<} \t\t\t\t{dobro(x, formato=True)}')
    print(f'{"Metade do Preço:":<} \t\t\t\t{metade(x, formato=True)}')
    print(f'{"Aumento do Preço em ":<}{aumento:<}%: \t\t{aumentar(x, aumento, formato=True)}')
    print(f'{"Redução do Preço em ":<}{reducao:<}%: \t\t{reduzir(x, reducao, formato=True)}')
    print('-' * 45)

