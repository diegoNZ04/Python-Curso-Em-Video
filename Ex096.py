def texto(text):
    print(text)
    print('-'*30)

def area():
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    a = largura * comprimento
    print(f'A área de um terreno {largura:.2}x{comprimento:.2} é de {a}')


texto('Controle de Terreno')
area()