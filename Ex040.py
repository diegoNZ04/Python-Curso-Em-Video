print('-=-' * 15)
print('\033[1;34mMÉDIA DO ALUNO\033[m')
print('-=-' * 15)
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
if m >= 7.0:
    print('O aluno está \033[32mAPROVADO\033[m')
elif m > 5.0 and m < 7.0:
    print('\033[33mO aluno está de RECUPERAÇÃO\033[m')
elif m < 5.0:
    print('\033[31mO aluno está REPROVADO\033[m')
