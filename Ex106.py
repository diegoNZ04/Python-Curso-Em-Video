def ajuda(prompt):
    print('\033[0;32m~\033[m' * 50)
    print(f'\033[1;32m      Acessando o manual de comando {prompt}\033[m')
    print('\033[0;32m~\033[m' * 50)
    return help(prompt)


while True:
    op = str(input('\033[0;36mFunção ou Biblioteca > \033[m')).lower().strip()
    if op in 'fim':
        break
    ajuda(op)
print('\033[1;32m<<< Programa Encerrado >>>\033[m')