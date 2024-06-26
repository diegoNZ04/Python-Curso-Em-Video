valores = list()
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
print('-=-'*20)
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} valores')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')