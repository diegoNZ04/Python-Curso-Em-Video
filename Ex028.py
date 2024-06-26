from random import randint
n1 = randint(1, 5)
n2 = int(input('Digite um número de 1 a 5:  '))
print(f'O número sorteado foi: {n1}')
if n1 == n2:
    print('Você acertou!')
else:
    print('Você errou!')

