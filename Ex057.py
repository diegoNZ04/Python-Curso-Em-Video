r = str(input('Qual o seu sexo? [M/F] ')).upper().strip()
while r != 'M' and r != 'F':
    if r != 'M' and r != 'F':
        r = str(input('Dados inválidos. Digite novamente: ')).upper().strip()
print(f'Sexo {r} registrado com sucesso!')