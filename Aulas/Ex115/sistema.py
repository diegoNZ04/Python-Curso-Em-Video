from Aulas.Ex115.lib.interface import *
from Aulas.Ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt.py'
if not arquivoExiste(arq):
    criarArquivo(arq)

#Programa Principal

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar novo conteúdo em um arquivo
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do Sistema...')
        sleep(0.5)
        cabecalho('<<< PROGRAMA FINALIZADO >>>')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
        sleep(0.5)