from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(oposto, adjacente):.2f}')