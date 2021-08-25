frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertida = junto[::-1]
print(f'O inverso de {junto} é {invertida}')
if junto == invertida:
    print('A frase digitada É um palíndromo!')
else:
    print('A frase digitada NÃO É um palíndromo!')
