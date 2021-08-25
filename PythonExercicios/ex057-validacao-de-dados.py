sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação incorreta, digite novamente [M/F]: ')).upper().strip()[0]
print(f'Obrigado! Seu sexo foi computado como {sexo}!')
