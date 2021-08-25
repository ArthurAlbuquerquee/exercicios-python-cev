valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = valor / (anos*12)
prestacao2 = salario * 30 / 100
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${prestacao:.2f} por mês! ')
if prestacao2 >= prestacao:
    print('Seu empréstimo foi \033[1;32mAPROVADO\033[m!')
else:
    print('Seu empréstimo foi \033[1;31mNEGADO\033[m!')
