from datetime import date
ano = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Usuário {c} - Digite seu ano de nascimento: '))
    idade = ano - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'{totalmaior} usuários são maiores de idade!')
print(f'{totalmenor} usuários são menores de idade!')