from random import randint
from time import sleep
escolha = int(input('''Qual das opções você deseja?
 [0] Pedra
 [1] Papel
 [2] Tesoura
 OPÇÃO: '''))
lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PO!!!')
print('-=-' * 10)
print(f'O computador escolheu {lista[computador]}')
print(f'Você escolheu {lista[escolha]}')
print('-=-' * 10)
if escolha == 0 and computador == 0:
    print('EMPATOU!')
elif escolha == 0 and computador == 1:
    print('VOCÊ PERDEU!')
elif escolha == 0 and computador == 2:
    print('VOCÊ GANHOU!')
elif escolha == 1 and computador == 0:
    print('VOCÊ GANHOU!')
elif escolha == 1 and computador == 1:
    print('EMPATOU!')
elif escolha == 1 and computador == 2:
    print('VOCÊ PERDEU!')
elif escolha == 2 and computador == 0:
    print('VOCÊ PERDEU!')
elif escolha == 2 and computador == 1:
    print('VOCÊ GANHOU!')
elif escolha == 2 and computador == 2:
    print('EMPATOU!')
else:
    print('\033[2;31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m')
