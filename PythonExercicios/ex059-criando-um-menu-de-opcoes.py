from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor:  '))
opcao = 0
while opcao != 5:
    escolha = print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>> Qual é a opção? '))
    if opcao == 1:
        print(f'A soma de {n1} + {n2} é igual a {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação de {n1} por {n2} é igual a {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número entre {n1} e {n2} é {maior}')
        elif n1 == n2:
            print('Os valores são iguais!')
        else:
            maior = n2
            print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
       print('\033[31mOpção inválida. Tente novamente!\033[m')
    sleep(2)

print('Fim do programa! Volte sempre!')
