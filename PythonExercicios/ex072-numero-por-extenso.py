numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    n = ' '
    continuar = ' '
    while n not in range(0, 21):
        n = int(input('Digite um número de 0 a 20: '))
        if n > 21:
            print('NÚMERO INVÁLIDO!', end=' ')
    print(f'Você digitou o número {numeros[n]}')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar not in 'SN':
            print('COMANDO INVÁLIDO!', end=' ')
    if continuar == 'N':
        break
print('Fim do programa!')
