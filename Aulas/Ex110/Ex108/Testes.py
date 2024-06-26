from Aulas.Ex109 import moedas

p = float(input('Digite  o preço: R$'))
print(f'A metade de {moedas.moeda(p)} é igual a {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é igual a {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando em 10%, temos {moedas.aumentar(p, 10)}')
