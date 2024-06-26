from random import randint
from time import sleep

valores = list()


def sorteia():
    print(f'Sorteando os valores: ', end='')
    for c in range(1, 6):
        n = randint(1, 10)
        valores.append(n)
        print(n, end=' ')
        sleep(0.5)
    print('FIM!')


def somapar():
    s = 0
    for num in valores:
        if num % 2 == 0:
            s += num
    print(f'A soma dos valores pares de {valores} é de {s}')


sorteia()
somapar()