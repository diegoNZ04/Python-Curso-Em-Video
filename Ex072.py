extensos = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
r = ''
while True:
    numero = int(input('Digite um número entre 0 a 20: '))
    if numero > 20:
        numero = int(input('Tente novamente. Digite um número entre 0 a 20: '))
    print(f'Você digitou o número {extensos[numero]}')
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
print('Programa Encerrado!')