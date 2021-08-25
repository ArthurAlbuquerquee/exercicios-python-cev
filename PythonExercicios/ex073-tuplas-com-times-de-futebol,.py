times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo',
         'Atlético-GO', 'Athletico-PR', 'Ceará SC', 'Internacional', 'Santos',
         'Corinthians', 'Juventude', 'Cuiabá', 'Bahia', 'São Paulo', 'Fluminense',
         'Grêmio', 'Sport Recife', 'América-MG', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:20]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª pisção')
