n = float(input('Qual o salário do funcionário? '))
if n <= 1250.00:
    print(f'O salário {n:.2f} aumenta para {n+((n/100)*15)}')
if n > 1250.00:
    print(f'O salário {n:.2f} aumenta para {n+((n/100)*10)}')