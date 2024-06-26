p = int(input('Primeiro Termo: '))
r = int(input('Razão do PA: '))
c = 10
pa = p
while c > 0:
    print(f"{pa} > ", end=" ")
    pa = pa + r
    c = c - 1
print('ACABOU!')