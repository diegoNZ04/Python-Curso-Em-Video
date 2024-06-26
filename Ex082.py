valores = list()
par = list()
impar = list()
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if v%2 == 0:
        par.append(v)
    else:
        impar.append(v)
    if r in 'Nn':
        break
print('-=-'*20)
valores.sort()
print(f'A lista completa é {valores}')
print(f'Os números pares na lista foram {par}')
print(f'Os números ímpares na lista foram {impar}')