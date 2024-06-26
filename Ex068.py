from random import randint
n = cont = total = 0
r = ''
print('-=-'*10)
print('VAMOS JOGAR IMPAR OU PAR!')
print('-=-'*10)
while True:
    n = int(input('Digite um valor [0 à 10]: '))
    r = str(input('Ímpar ou Par? [I/P]: ')).upper().strip()[0]
    pc = randint(0, 10)
    total = n + pc
    if total % 2 == 0:
        print('-'*20)
        print(f'Você jogou {n} e o computador {pc}. Total: {total} (PAR)')
        print('-' * 20)
    else:
        print('-' * 20)
        print(f'Você jogou {n} e o computador {pc}. Total: {total} (ÍMPAR)')
        print('-' * 20)
    if r in 'Pp' and total % 2 == 0:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    elif r in 'Pp' and total % 2 != 0:
        print('VOCÊ PERDEU!')
        break
    elif r in 'Ii' and total % 2 != 0:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    elif r in 'Ii' and total % 2 == 0:
        print('VOCÊ PERDEU!')
        break
print(f'Você teve {cont} vitória(s) até perder!')