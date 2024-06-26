km = float(input('Digite a distância da viagem em km: '))
if km <= 200:
    print(f'Sua viagem custa {km*0.50}')
else:
    print(f'Sua viagem custa {km*0.45}')