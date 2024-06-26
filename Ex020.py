import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
deck = [n1, n2, n3, n4]
order = random.shuffle(deck)
print(f'A ordem de apresentação será')
print (order)
