print('\033[35m¬' * 9, 'Calculador de tabuada', '¬' * 9)
num = int(input('\033[32mVocê quer saber a tabuada de qual numero? \033[m'))
print('¬¬-' * 14)
while True:
    for c in range(1, 11):
        print(f'{num} x {c:>2} = {c * num}')
    print('¬' * 43)
    num = int(input('\033[32mVocê quer saber a tabuada de  qual número? \033[m'))
    if num < 0:
        break
print('\033[31mPrograma finalizado\033[m')

# O que eu poderia melhorar: poderia ter colocado o While logo de início, pois ele não está pedindo o valor de num antes
# de While.
