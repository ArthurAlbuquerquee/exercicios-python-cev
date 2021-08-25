from random import randint
from time import sleep
print('-'*56)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-'*56)
escolha = randint(0, 5)
n1 = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(1.5)
if n1 == escolha:
    print(f'Parabéns, você acertou! Eu pensei no número {escolha}')
else:
    print(f'Que pena, você errou! Eu pensei no número {escolha}')
