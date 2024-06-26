p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
for c in range(p, 11, r):
    print(f'{c} ->', end=' ')
print('ACABOU!')