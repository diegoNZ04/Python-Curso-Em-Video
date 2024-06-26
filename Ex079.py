valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor repetido! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
print('-=-'*30)
valores.sort()
print(f'Você digitou os valores: {valores}')