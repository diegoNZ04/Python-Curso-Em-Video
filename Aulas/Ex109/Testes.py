import moedas

p = float(input('Digite  o preço: R$'))
print(f'A metade de {moedas.moeda(p)} é igual a {moedas.metade(p, False)}')
print(f'O dobro de {moedas.moeda(p)} é igual a {moedas.dobro(p, False)}')
print(f'Aumentando em 10%, temos {moedas.aumentar(p, 10, False)}')
print(f'Reduzindo em 13%, temos {moedas.reduzir(p, 13, False)}')