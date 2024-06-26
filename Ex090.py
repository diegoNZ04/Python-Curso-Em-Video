aluno = dict()
classe = list()
aluno['nome'] = str(input('Nome do Aluno: '))
aluno['media'] = float(input('Média do Aluno: '))
classe.append(aluno.copy())
print('-=-'*30)
print(f'O nome do aluno é {aluno['nome']}')
print(f'A média do aluno é {aluno['media']}')
if aluno['media'] >= 7:
    print('O aluno está aprovado!')
elif aluno['media'] >= 5:
    print('O aluno está de recuperação!')
elif aluno['media'] <= 4:
    print('O aluno está reprovado!')