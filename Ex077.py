palavra = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'ESTUDAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
