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


def leiaFloat(prompt):
    while True:
        try:
            real = float(input(prompt))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não informar este número.\033[m')
            return 0
        else:
            return real


# Programa Principal
inteiro = leiaInt('Número Inteiro: ')
real = leiaFloat('Número Real: ')

print(f'Você digitou os números {inteiro} e {real}')