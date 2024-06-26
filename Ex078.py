valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na Posição {cont}: ')))
print('-=-'*20)
print(f'Você digitou os valores {valores}')
maior = max(valores)
menor = min(valores)
print(f'O menor número achado na lista foi {menor} na Posição ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos} ', end='')
print()
print(f'O maior número achado na lista foi {maior} na Posição ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos} ', end='')
print()