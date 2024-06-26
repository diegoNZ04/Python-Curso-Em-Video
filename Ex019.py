import random
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
escolhido = random.choice([al1, al2, al3])
print(f'O aluno escolhido foi {escolhido}')