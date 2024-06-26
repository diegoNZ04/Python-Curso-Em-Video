n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    for c in range (1, 11):
        print(f'{n} X {c} = {n * c}')
    print('-'*20)
    if n < 0:
        break
print('PROGRAMA DE TABUADA ENCERRADO!')