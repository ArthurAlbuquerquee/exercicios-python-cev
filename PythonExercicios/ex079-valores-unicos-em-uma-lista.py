numeros = list()
while True:
    continuar = ' '
    add = int(input('Digite um número: '))
    if add not in numeros:
        numeros.append(add)
        print('\033[1:32mNúmero adicionado com sucesso!\033[m')
    elif add in numeros:
        print('\033[1:31mO número não foi adicionado, pois já existe!\033[m')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar not in 'SN':
            print('\033[1:31mOPÇÃO INVÁLIDA!\033[m', end=' ')
    if continuar == 'N':
        break
print('Você digitou os valores ', end='')
for c in sorted(numeros):
    print(c, end=' ')
