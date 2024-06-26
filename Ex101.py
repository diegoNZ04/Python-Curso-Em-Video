from datetime import date


def voto(ano=0):
    ano = date.today().year
    i = ano - data
    if i < 18:
        return f'Sua idade é de {i} anos. NÃO VOTA.'
    if i < 18 or i >= 70:
        pass
    else:
        return f'Sua idade é de {i} anos. VOTO OBRIGATÓRIO'
    if i >= 70:
        return f'Sua idade é de {i} anos. VOTO OPCIONAL'


data = int(input('Informe a data do seu nascimento: '))
print(voto(data))