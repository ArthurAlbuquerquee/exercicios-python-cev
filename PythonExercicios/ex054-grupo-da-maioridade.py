from datetime import date
ano = date.today().year
soma = 0
cont = 0
cont2 = 0
for c in range(1, 8):
    idade = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if ano - idade >= 21:
        cont = cont + 1
print(f'{cont} pessoas já são de maior')
print(f'{7 - cont} pessoas ainda não são de menor')
