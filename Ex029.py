km = int(input('Digite a velocidade: '))
if km > 80:
    print('Você ultrapassou a velocidade máxima!')
    print(f'Sua multa é de {(km-80)*7} ')
else:
    print('Você está dentro da velocidade permitida!')