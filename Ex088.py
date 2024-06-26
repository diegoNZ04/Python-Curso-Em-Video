from time import sleep
from random import sample
print('-'*40)
print(f'{"JOGA NA MEGASENA":^40}')
print('-'*40)

for c in range(int(input('Números de Jogos: '))):
    print(f'Jogo {c+1}: {sample(range(1, 61), 6)}')
    sleep(0.5)