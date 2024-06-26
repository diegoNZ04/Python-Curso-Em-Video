r = 'S'
n = soma = media = cont = maiornum = menornum = 0
while r in 'Ss':
    n = int(input('Digite um valor: '))
    cont += 1
    soma += n
    media = soma/cont
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 1:
        maiornum = menornum = n
    else:
        if n > maiornum:
            maiornum = n
        if n < menornum:
            menornum = n
print(f'''Você digitou {cont} números e a média foi {media}
O menor número digitado foi {menornum} e o maior número digitado foi {maiornum}''')
