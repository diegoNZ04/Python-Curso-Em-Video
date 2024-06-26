from random import randint
pc = randint(0, 10)
tentativas = 0
n = int(input('Digite um número de 0 até 10: '))
while n != pc:
    n = int(input(f'Você errou! Tente outra vez. Digite outro número: '))
    tentativas += 1
print(f'O número pensado foi {pc}, você acertou!')
print(f'Você precisou de {tentativas+1} tentativa(s)!')