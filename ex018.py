from math import tan, sin, cos, radians
angulo = float(input('Digite um ângulo para saber o seno, consseno e tangente: '))
radian = radians(angulo)
seno = sin(radian)
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}.')
cosseno = cos(radian)
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}.')
tangente = tan(radian)
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}.')
#CORRIGIDO
