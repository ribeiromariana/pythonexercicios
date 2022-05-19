def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno de {larg}X{comp} é de {a:.1f}m²!')


# Programa principal
print(f'{"      Calculador de Terrenos!":^20}')
print('¬¬' * 18)
l = float(input('Largura do terreno: (m)'))
c = float(input('Comprimento do terreno: (m)'))
area(larg=l, comp=c)
