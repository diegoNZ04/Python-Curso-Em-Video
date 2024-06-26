print('-=-'*15)
print('\033[1;34mÍndice de Massa Corporal\033[m')
print('-=-'*15)
a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
imc = p/(a**2)
print(f'Seu IMC é de {imc:.1f}!')
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA!')