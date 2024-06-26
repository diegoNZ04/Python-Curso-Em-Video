def leiaInt(prompt):
    while True:
        try:
            inteiro = int(input(prompt))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não informar este número.\033[m')
            return 0
        else:
            return inteiro


def linha(tam=42):
    return '-' * tam


def cabecalho(prompt):
    print(linha())
    print(prompt.center(42))
    print(linha())


def menu(lst):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lst:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

