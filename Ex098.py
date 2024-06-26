from time import sleep


def contador(i, f, p):
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')


#Programa Principal

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = abs(int(input('Passo: ')))
contador(ini, fim, pas)