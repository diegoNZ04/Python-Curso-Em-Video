from datetime import date
d = date.today().year
a = int(input('Ano de nascimento do atleta: '))
i = d - a
print(f'O atleta tem {i} ano(s)!')
if i <= 9:
    print('Classificação: MIRIM')
elif i > 9 and i <= 14:
    print('Classificação: INFANTIL')
elif i >= 15 and i <= 19:
    print('Classificação: JÚNIOR')
elif i >= 20 and i <=25:
    print('Classificação: SÊNIOR')
elif i > 25:
    print('Classificação: MASTER')