numeros = int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: '))
print(f'Você digitou os números: {numeros}')
print(f'O número 9 aparece {numeros.count(9)} vezes')
print(f'O número 3 aparece na {numeros.index(3)+1}° posição na primeira ocorrência')
for n in numeros:
    if n % 2 == 0:
        print(f'Os valores pares digitados foram: {n}')