print('{:=^40}'.format('\033[1mLOJAS ALBUQUERQUE\033[m'))
preco = float(input('Qual o valor do produto? R$'))
pagamento = int(input('''Qual a forma de pagamento?
[1] À vista no Dinheiro/Cheque (10% de desconto)
[2] À vista no Cartão de crédito (5% de desconto)
[3] Em até 2x no Cartão de crédito
[4] Em até 3x ou mais no Cartão de crédito (20% de juros)
OPÇÃO: '''))
if pagamento == 1:
    total = preco - (preco * 10 / 100)
elif pagamento == 2:
    total = preco - (preco * 5 / 100)
elif pagamento == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x sem juros de R${parcela:.2f}')
elif pagamento == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Em quantas parcelas?'))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x com juros de R${parcela:.2f}')
else:
    total = preco
    print('\033[2;31mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.\033[m')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final')
