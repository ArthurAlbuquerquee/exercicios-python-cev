palavras = ('jogar', 'brincar', 'programar', 'estudar',
            'dialogar', 'criar', 'inventar', 'plantar',
            'pescar', 'lanchar', 'escovar', 'jantar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
