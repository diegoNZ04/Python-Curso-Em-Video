from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['ctps'] = int(input('N° Carteira de Trabalho [0 caso não tenha]: '))

def mostrar_dados_basicos(trabalhador):
    print('-=-' * 30)
    print(f'Nome: {trabalhador['nome']}')
    print(f'Idade: {trabalhador['idade']}')
    print(f'N°da Carteira de Trabalho: {trabalhador['ctps']}')

def dados_trabalhistas(trabalhador):
    trabalhador['contrato'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Valor do Salário: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contrato'] + 35) - datetime.now().year)

def mostrar_dados_totais(trabalhador):
    print('-=-' * 30)
    mostrar_dados_basicos(trabalhador)
    print(f'Ano de Contratação: {trabalhador['contrato']}')
    print(f'Valor do Salário: {trabalhador['salario']}')
    print(f'Trabalhador vai se aposentar com {trabalhador['aposentadoria']} anos')


if trabalhador['ctps'] == 0:
    mostrar_dados_basicos(trabalhador)

else:
    dados_trabalhistas(trabalhador)
    mostrar_dados_totais(trabalhador)