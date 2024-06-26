from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
'jogador1': randint(1, 6),
'jogador2': randint(1, 6),
'jogador3': randint(1, 6),
'jogador4': randint(1, 6),
}
print('-=-'*30)
print('Valores Sorteados: ')
for k, v in jogadores.items():
    print(f'O {k} obteve o valor {v}.')
    sleep(0.5)
print()
print('-=-'*30)
print('RANKING DO JOGO')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
