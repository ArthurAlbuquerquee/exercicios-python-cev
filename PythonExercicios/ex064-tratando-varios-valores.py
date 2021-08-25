n = int(input('Informe um número [999 para parar]: '))
cont = 0
soma = 0
while n != 999:
   cont = cont + 1
   soma = soma + n
   n = int(input('Informe um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
print('FIM')
