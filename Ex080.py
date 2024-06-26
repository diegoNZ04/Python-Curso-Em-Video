valores = list()
for cont in range(0,5):
    v = int(input('Digite um valor: '))
    for pos, valor in enumerate(valores):
        if v < valor:
            valores.insert(pos, v) #definir posição onde o elementro entra caso for menor
            print(f'Número {v} entra na Posição {pos}')
            break
    else:
        valores.append(v)
        print(f'Número {v} entra na Posição Final...')
print(f'Lista atual: {valores}')