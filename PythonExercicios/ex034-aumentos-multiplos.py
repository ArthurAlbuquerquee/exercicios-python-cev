salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    aumento1 = salario * 15 / 100 + salario
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento1:.2f}')
else:
    aumento2 = salario *10 / 100 + salario
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento2:.2f}')
