string = str(input('Digite uma frase: ')).replace(' ', '').lower().strip()
string_inversa = string[::-1]
print(f'A frase {string} de trás para frente é {string_inversa}')
if string == string_inversa:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')