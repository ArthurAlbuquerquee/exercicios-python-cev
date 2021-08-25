peso = float(input('Qual o seu peso? (Kg)  '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / altura ** 2
print(f'O seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc < 30:
    print('Você está com sobrepeso!')
elif imc < 40:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você está com obesidade mórbida!')
