lista = list()
partidas = list()
dados = dict()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    jogos = int(input(f'Quantos jogos {dados['nome']} disputou? '))
    partidas.clear()
    for c in range(1, jogos+1):
        partidas.append(int(input(f' - Quantos gols na {c}° partida? ')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    lista.append(dados.copy())
    while True:
        r = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if r == 'N':
        break
print('-='*50)
print(f'{"cod":>4} ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for k, v in enumerate(lista):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    print('-'*50)
    op = int(input('Mostrar dados de qual jogador? [999 para encerrar]: '))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op >= len(lista):
        print(f'ERRO! Não existe jogador com o código {op}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[op]['nome']}')
        for i, g in enumerate(lista[op]["gols"]):
            print(f'    => No jogo {i+1}, fez {g} gols')
print('PROGRAMA ENCERRADO!')