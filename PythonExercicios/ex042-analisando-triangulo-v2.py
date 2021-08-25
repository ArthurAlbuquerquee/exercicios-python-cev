r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r1 == r3 and r2 == r3:
     print('Forma um triângulo EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
     print('Forma um triângulo um ISÓSCELES!')
    else:
     print('Forma um triângulo ESCALENO')
else:
    print('NÃO forma um triângulo')
