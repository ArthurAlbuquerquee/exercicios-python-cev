from random import randint
cont = 0
escolha = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
n = int(input('Qual é o seu palpite? '))
while n != escolha:
    if n < escolha:
        n = int(input('''Mais... Tente mais uma vez.
Qual é o seu palpite? '''))
    if n > escolha:
        n = int(input('''Menos... Tente mais uma vez.
Qual é o seu palpite? '''))
    cont = cont + 1
print(f'Você acertou na {cont+1}ª tentativa!')
