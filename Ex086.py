m = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        m[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{m[l][c]:^5}', end='')
    print()