from datetime import date
n = int(input('Qual o ano atual? Coloque 0 para analisar o ano atual: '))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f'O ano {n} é BISSEXTO')
else:
    print(f'O ano {n} não é BISSEXTO')