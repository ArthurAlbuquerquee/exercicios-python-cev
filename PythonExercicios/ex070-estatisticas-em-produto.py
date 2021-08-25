print('=' * 30)
print('{:^30}'.format('LOJA ALBUQUERQUE'))
print('=' * 30)
tot = contmil = cont = menor = 0
batato = ''
while True:
    continuar = ' '
    produto = str(input('Nome do Produto: ')).capitalize()
    preco = float(input('Preço: R$'))
    tot = tot + preco
    cont = cont + 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 1000:
        contmil = contmil + 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('------ FIM DO PROGRAMA ------')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {contmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
