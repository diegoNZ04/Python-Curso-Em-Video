classe = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    classe.append(dados[:])
    dados.clear()
    r = str(input('Você quer continuar? [S/N]: '))
    if r in 'Nn':
        break

#Solução do Professor Para Listas Compostas
'''Ficha = list()
while True:
    nome = str(input('Nome: ')))
    nota 1 = float(input('Nota 1: ')))
    nota 2 = float(input('Nota 2: ')))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Você quer continuar? [S/N]: '))
    if r in 'Nn':
        break'''

print('-=-'*30)
print('No.  ', end='')
print(f'{"Nome":^10}', end='')
print(f'{"Média":^18}')
print('-'*30)
for cont, alunos in enumerate(classe):
    print(cont, end='')
    media = (alunos[1] + alunos[2])/2
    print(f'{alunos[0]:^20}', end='')
    print(f'{media:^5}')
while True:
    print('-' * 30)
    op = int(input('Mostrar notas de qual aluno? [999 para encerrar]: '))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op <= len(classe) - 1:
        print(f'Notas de {classe[op][0]} são {classe[op][1]} e {classe[op][2]}')
print('PROGRAMA FINALIZADO!')