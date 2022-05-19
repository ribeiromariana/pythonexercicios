#AINDA NÃO ESTUDEI ESSE CONSEITO EM MATEMÁTICA ;-;
'''cateto_oposto = float(input('Medida do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f'A hipotenusa mede {hipotenusa:.2f}')'''

from math import hypot
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoAdjacente, catetoOposto)
print(f'A hipotenusa é {hipotenusa:.2f}.')
#CORRIGIDO
