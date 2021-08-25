from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
print(f'O Seno de {angulo} é {sin(radians(angulo)):.2f}')
print(f'O Cosseno de {angulo} é {cos(radians(angulo)):.2f}')
print(f'A Tangente de {angulo} é {tan(radians(angulo)):.2f}')