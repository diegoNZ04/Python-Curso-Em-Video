lista = list()
dados = dict()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]

        if dados['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        r = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if r == 'N':
        break

print('-=-' * 30)
media = soma / len(lista)
print(f'A) No total foram {len(lista)} pessoas cadastradas.')
print(f'B) A média das idades foi de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}', end='. ')
print()
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in lista:
    if p['idade'] >= media:
        print(f'    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')