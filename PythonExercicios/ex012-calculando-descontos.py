valor = float(input('Qual o preço do produto? R$'))
des = 5 * valor / 100
print(f'O produto que custava R${valor:.2f}, na promoção com 5% de desconto vai custar R${valor-des:.2f}')

