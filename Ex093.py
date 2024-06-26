partidas = list()
dados = dict()
dados['nome'] = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantos jogos {dados['nome']} disputou? '))

for c in range(1, jogos+1):
    partidas.append(int(input(f' - Quantos gols na {c}° partida? ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('-=-'*30)
print(dados)
print('-=-'*30)
for k, v in dados.items():
    print(f'No campo {k} temos o valor {v}')
print('-=-'*30)
print(f'O jogador {dados['nome']} jogou {jogos} partidas.')
for i, v in enumerate(dados['gols']):
    print(f' => Na partida {i+1}, fez {v} gols.')