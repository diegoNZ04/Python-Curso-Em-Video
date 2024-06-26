from random import randint
deck = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
u = int(input('Qual a sua jogada? '))
print(f'Eu escolhi {deck[pc]}!')
if pc == 0:
    if u == 0:
        print('EMPATE')
    elif u == 1:
        print('JOGADOR VENCE')
    elif u == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1:
    if u == 0:
        print('JOGADOR PERDE')
    elif u == 1:
        print('EMPATE')
    elif u == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2:
    if u == 0:
        print('JOGADOR VENCE')
    elif u == 1:
        print('JOGADOR PERDE')
    elif u == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
