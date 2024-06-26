r = ''

print('=='*15)
print('{:^30}'.format('BANCO FAZ O L'))
print('=='*15)

while True:
    valor = int(input('Digite o valor do saque: '))
    cont50 = valor // 50
    valor %= 50
    cont20 = valor // 20
    valor %= 20
    cont10 = valor // 10
    valor %= 10
    cont1 = valor // 1
    print('==' * 10)
    print(f'''Total de {cont50} cédulas de R$50 sacadas
Total de {cont20} cédulas de R$20 sacadas
Total de {cont10} cédulas de 10 sacadas
Total de {cont1} cédulas de 1 sacadas''')
    print('==' * 10)
    r = str(input('Deseja sacar mais valores? [S/N] ')).upper().strip()[0]
    if r in 'Nn':
        break
print('Muito obrigado. Volte sempre!')