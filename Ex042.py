print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
n1 = float(input('Digite o tamanho do 1° lado: '))
n2 = float(input('Digite o tamanho do 2° lado: '))
n3 = float(input('Digite o tamanho do 3° lado: '))
if (n1 + n2) > n3 and (n1 + n3) > n2 and (n2 + n3) > n1:
    print('Os lados acima PODEM formar um triângulo!', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os lados acima NÃO PODEM formar um triângulo!')
