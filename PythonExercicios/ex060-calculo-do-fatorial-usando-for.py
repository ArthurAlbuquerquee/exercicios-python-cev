n = int(input('Digite um número para calcular o fatorial: '))
f = 1
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
print(f'{f}')
