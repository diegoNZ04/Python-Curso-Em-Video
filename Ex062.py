numero = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

cont = 0
calculo_da_PA = numero

a_mais = 10
total = 0

while a_mais != 0:
    total = total + a_mais
    while cont < total:
        print(f'{calculo_da_PA} > ', end=' ')
        calculo_da_PA = calculo_da_PA + razao
        cont += 1
    print('PAUSA')
    a_mais = int(input('Quantos números você quer mostrar a mais? '))
print(f'Progressão finalizada com {cont} termos mostrados')