print('\033[34m======== LOJAS AMORIM ========\033[m')
v = float(input('Informe o valor total das compras: '))
print('''\033[32mFORMAS DE PAGAMENTO\033[m
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    print(f'O valor final da compra é R${v-((v/100)*10):.2f}')
elif op == 2:
    print(f'O valor final da compra é R${v - ((v / 100) * 5):.2f}')
elif op == 3:
    print(f'O valor final da compra foram de duas parcelas mensais de  R${v/2:.2f}')
elif op == 4:
    p = int(input('Quantas parcelas? '))
    t = v+((v/100)*20)
    print(f'Sua compra será parcelada em {p}x de R${t/p:.2f} com 20% DE JUROS AO MÊS')
    print(f'Sua compra de R${v:.2f} vai custa {t:.2f} no final')