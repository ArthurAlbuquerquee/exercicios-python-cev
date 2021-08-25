from random import randint
print('-=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 10)
v = 0
while True:
    n = int(input('Diga um valor: '))
    pc = randint(1, 10)
    soma = n + pc
    soma2 = soma % 2
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-' *55)
    print(f'Você jogou {n} e o computador {pc}. Total de {soma}, ', end='')
    print('DEU PAR' if soma2 % 2 == 0 else 'DEU IMPAR')
    if pi == 'P':
        if soma2 == 0:
            print('VOCÊ GANHOU!')
            v = v + 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif pi == 'I':
        if soma2 != 0:
            print('VOCÊ VENCEU!')
            v = v + 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-'*55)
print(f'GAME OVER! Você venceu {v} vezes')
print('-'*55)