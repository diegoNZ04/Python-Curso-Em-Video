def leiadinheiro(prompt):
    ok = False
    while not ok:
        entrada = str(input(prompt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" é um Preço Inválido!\033[m')
        else:
            ok = True
            return float(entrada)


def leiaInt(prompt):
    ok = False
    valor = 0
    while True:
        n = str(input(prompt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor