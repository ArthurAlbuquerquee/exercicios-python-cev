from datetime import date
sexo = int(input('''Qual o seu sexo?
[1]Masculino
[2]Feminino
Opção: '''))
if sexo == 1:
    atual = date.today().year
    idade = int(input('Qual seu ano de nascimento? '))
    calculo = atual - idade
    print(f'Quem nasceu em {idade} tem {calculo} anos em {atual}')
    if sexo == 1 and calculo == 18:
        print('Está na hora de se alistar!')
    elif sexo == 1 and calculo < 18:
        print(f'Faltam {18-calculo} anos para se alistar')
        print(f'Seu alistamento será em {idade + 18}')
    elif sexo == 1 and calculo > 18:
        print(f'Você deveria já ter se alistado há {calculo-18} anos')
        print(f'Seu alistamento foi em {idade + 18}')
elif sexo == 2:
    print('seu alistamento NÃO É OBRIGATÓRIO!')
