preco = total = mais_1000 = valor_barato = cont = 0
r = produto = nome_barato = ''

print('-=-'*10)
print('SUPER LOJAS BARATÃO')
print('-=-'*10)

while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço do Produto: R$'))
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    total += preco
    cont += 1
    if preco >= 1000:
        mais_1000 += 1
    if cont == 1:
        valor_barato = preco
        nome_barato = produto
    else:
        if preco < valor_barato:
            valor_barato = preco
            nome_barato = produto
    if r in 'Nn':
        break
print(f'''O total da compra foi de R${total}
{mais_1000} custaram mais de R$1000
{nome_barato} foi o produto mais barato e custou R${valor_barato}''')