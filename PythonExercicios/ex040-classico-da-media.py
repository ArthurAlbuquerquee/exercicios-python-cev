n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}')
if media <= 5:
    print('O aluno está \033[31mREPROVADO\033[m!')
elif media <= 6.9:
    print('O aluno está de \033[33mRECUPERAÇÃO\033[m!')
elif media >= 7:
    print('O aluno está \033[32mAPROVADO\033[m!')
