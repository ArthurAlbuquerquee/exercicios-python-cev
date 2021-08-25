primeirot = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeirot
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo = termo + razao
    cont = cont + 1
print('Fim')
