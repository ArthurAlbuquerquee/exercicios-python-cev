mts = float(input('Escolha quantos metros deseja converter: '))
km = mts * 0.001
hm = mts * 0.01
dam = mts * 0.1
m = mts * 1
dm = mts * 10
cm = mts * 100
mm = mts * 1000
print(f'A média de {mts} corresponde a: ')
print(f'{km}km \n{hm}hm \n{dam:.1f}dam \n{m:.0f}m \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm ')