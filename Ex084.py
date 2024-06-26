lista_pessoas = list()
lista_dados = list()
totpessoas = maior = menor = 0
while True:
    lista_dados.append(str(input('Nome: ')))
    lista_dados.append(float(input('Peso: ')))
    if len(lista_pessoas) == 0:
        maior = menor = lista_dados[1]
    else:
        if lista_dados[1] > maior:
            maior = lista_dados[1]
        if lista_dados[1] < menor:
            menor = lista_dados[1]
    lista_pessoas.append(lista_dados[:])
    lista_dados.clear()
    totpessoas += 1
    r = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
print('-=-'*30)
print(f'Ao todo você cadastrou {totpessoas} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista_pessoas:
    if p[1] == maior:
        print(p[0], end=', ')
print('...')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in lista_pessoas:
    if p[1] == menor:
        print(p[0], end=', ')
print('...')