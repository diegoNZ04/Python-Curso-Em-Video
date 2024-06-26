n = int(input('Digite um valor: '))
primo = 0
for c in range(1, n+1):
    if n % c == 0:
        primo += 1
if primo == 2:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')

