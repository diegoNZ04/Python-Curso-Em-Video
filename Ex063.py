'''Sequência de Fibonacci'''

n = int(input('Quantos termos você quer? ')) #definir a quantidade de termos
a = 0
b = 1
c = 0
cont = 0
while cont < n: #condição de parada, enquanto cont for menor que n o laço de repetição retorna
    print(f'{c} > ', end=' ')
    a = b
    b = c
    c = a + b
    cont += 1 #para cada vez que o laço repetir, contador soma 1 até chegar condição de parada
print('FIM')



