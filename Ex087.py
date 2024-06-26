m = [[], [], []]
par = col3 = 0
for l in range(0, 3): #defini contador em linha
    for c in range(0, 3): #defini contador em coluna
        m[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
        if m[l][c] % 2 == 0: #soma dos pares
            par += m[l][c]
        if c == 2: #soma terceira coluna
            col3 += m[l][c]
print('-=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{m[l][c]:^5}', end='') #mostra coluna e linhas aninhando for
    print()
print('-=-'*30)
print(f'A soma dos números pares presentes na matriz é: {par}')
print(f'A soma dos números da terceira coluna é: {col3}')
print(f'O maior valor da segunda linha é {max(m[1])}')