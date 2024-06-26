print('--=--'*15)
print('\033[1;34mANÁLISE DE EMPRÉSTIMO\033[m')
print('--=--'*15)
v = float(input('Qual o valor da casa? '))
s = float(input('Qual o salário do comprador? '))
a = float(input('Em quantos anos o comprador pretende pagar? '))
p = v/(a*12)
if p > ((s/100)*30):
    print('Seu empréstimo foi \033[1;31mNEGADO\033[m')
else:
    print('Seu empréstimo foi \033[32mACEITO\033[m')