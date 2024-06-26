from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(numeros)
menor_valor = min(numeros)
maior_valor = max(numeros)
print(f'O menor valor encontrado foi {menor_valor}')
print(f'O maior valor encontrado foi: {maior_valor}')