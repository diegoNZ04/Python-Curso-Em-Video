from datetime import date
i = date.today().year
a = int(input('Informe o ano de seu nascimento: '))
print(f'Você tem {i-a} anos!')
sm = i-a
if sm < 18:
    print('Você ainda vai se alistar ao serviço militar obrigatório!')
    print(f'Após {18-sm} ano(s) você deve alistar!')
elif sm == 18:
    print('Já está na hora de você se alistar ao serviço militar obrigatório!')
elif sm > 18:
    print('Já passou do tempo de alistamento!')
    print(f'O prazo foi ultrapassado em {sm-18} ano(s)!')