idade = mais_18 = h_cadastrados = m_menos20 = 0
sexo = r = ''
while True:
    print('-=-'*10)
    print('CADASTRE UMA PESSOA')
    print('-=-' * 10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('--' * 10)
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    print('--' * 10)
    if idade >= 18:
        mais_18 += 1
    if sexo in 'Mm':
        h_cadastrados += 1
    if sexo in 'Ff' and idade < 20:
        m_menos20 += 1
    if r in 'Nn':
        break
print(f'''Foram cadastrados:
{mais_18} pessoas maiores de 18 anos
{h_cadastrados} homens cadastrados
{m_menos20} mulheres com menos de 20 anos
PROGRAMA ENCERRADO!''')