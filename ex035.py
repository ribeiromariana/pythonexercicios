reta1 = float(input('Valor da reta 1: '))
reta2 = float(input('Valor da reta 2: '))
reta3 = float(input('Valor da reta 3: '))
# Descobrindo qual reta é a maior, e somando as menores para usar depois.
menores = reta2 + reta3
maior = reta1
if reta2 > reta1 and reta2 > reta3:
    menores = reta1 + reta3
    maior = reta2
else:
    menores = reta2 + reta1
    maior = reta3
# Teste matemático para saber se da para formar o triângulo.
if menores > maior:
    resultado = 'é possível formar um triângulo!'
else:
    resultado = 'não é possível formar um triângulo.'
print(f'Com as retas acima, {resultado}')
