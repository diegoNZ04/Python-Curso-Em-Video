expr = str(input('Digite a expressão: '))
if expr.count('(') == expr.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')