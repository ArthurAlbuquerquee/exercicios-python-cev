print('-' * 30)
print('     CADASTRE UMA PESSOA')
print('-' * 30)
icont = 0
hcont = 0
mcont = 0
while True:
    sexo = ' '
    continuar = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        print('-' * 30)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    else:
        print('-' * 30)
        print('CADASTRE UMA PESSOA')
        print('-' * 30)
    if idade > 18:
        icont = icont + 1
    if sexo == 'M':
        hcont = hcont + 1
    if sexo == 'F' and idade < 20:
        mcont = mcont + 1
    if continuar == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {icont}')
print(f'Ao todo temos {hcont} homens cadastrados')
print(f'E temos {mcont} mulheres com menos de 20 anos')
