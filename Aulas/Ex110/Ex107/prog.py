from Aulas.Ex109 import moedas

p = float(input('Digite  o preço: R$'))
print(f'A metade de {p} é igual a {moedas.metade(p)}')
print(f'O dobro de {p} é igual a {moedas.dobro(p)}')
print(f'Aumentando em 10%, temos {moedas.aumentar(p, 10)}')
print(f'Diminuindo em 13%, temos {moedas.reduzir(p, 13)}')