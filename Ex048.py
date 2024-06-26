s = 0
st = 0
for c in range(3, 501, 6):
    s += c
    st += 1
print(f'A soma dos {st} valores múltiplos de três e ímpares entre 1 e 500 é {s}')