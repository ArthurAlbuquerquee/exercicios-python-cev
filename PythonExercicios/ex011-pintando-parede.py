altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
parede = largura*altura
litros = parede/2
tinta = parede*litros
print(f'Sua parede tem uma dimensão de {altura}x{largura} e sua área é de {parede}m²')
print(f'Precisa de {litros:.1f}L para pintar a parede')
