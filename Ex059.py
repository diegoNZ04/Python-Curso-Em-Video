n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
r = 1
while r != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior Número
[ 4 ] Novos Números
[ 5 ] Sair do Programa''')
    print('-=-'*10)
    r = int(input('>>> Qual a sua opção? '))
    print('-=-'*10)
    if r == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    if r == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
    if r == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n1 == n2:
            print('Os valores são iguais!')
        else:
            print(f'O maior número é {n2}')
    if r == 4:
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
print('Programa encerrado!')