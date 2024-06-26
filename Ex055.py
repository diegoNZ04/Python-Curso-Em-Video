maiorpeso = 0
menorpeso = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}° Pessoa: '))
    if peso == 1:
        maiorpeso = p
        menorpeso = p
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O maior peso lido foi de {maiorpeso}kg!')
print(f'O menor peso lido foi de {menorpeso}kg!')