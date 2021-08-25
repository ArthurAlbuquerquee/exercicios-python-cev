nome = str(input('Escreva seu nome completo: ')).strip()
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#Outra maneira de fazer o último print:

separa = nome.split()
#print('Seu primeiro nome é {} e ele tem letras'.format(separa[0], len (separa[0])))