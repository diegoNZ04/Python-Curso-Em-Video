def notas(* valores, sit=False):
    """
    Define a quantidade de notas, a maior e menor nota, calcula média e a situação dos alunos (opcional)
    :param valores: As notas dos alunos
    :param sit: (opcional) True para mostrar a situação, False para não mostrar
    :return: Mostra os dados calculados e definidos
    """
    s = 0
    for num in valores:
        s += num
    quant = len(valores)
    media = s / quant
    maior = max(valores)
    menor = min(valores)
    dados = {'quantidade': quant, 'maior': maior, 'menor': menor, 'media': media}
    if sit:
        if dados['media'] >= 7:
            dados['sit'] = 'APROVADO!'
        else:
            dados['sit'] = 'REPROVADO!'
    return dados


# Programa Principal
resp = notas(5.5, 10, 8.5)
print(resp)
