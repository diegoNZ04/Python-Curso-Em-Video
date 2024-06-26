n1 = int(input('\033[31mDigite um número: \033[m')) #definir variável n
n2 = int(input('\033[34mDigite mais um número: \033[m'))
s = n1 + n2 #variável soma
print(f'A soma de \033[31m{n1}\033[m e \033[34m{n2}\033[m é \033[33m{s}\033[m')