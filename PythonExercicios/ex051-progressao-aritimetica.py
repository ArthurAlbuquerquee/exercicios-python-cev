primeirot = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeirot + (10 - 1) * razao
for c in range(primeirot, decimo + razao, razao):
    print(c, end=' > ')
print('ACABOU!')
