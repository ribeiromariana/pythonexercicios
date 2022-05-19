num = int(input('Digite um número inteiro para saber a sua tabuada: '))
print('\033[33m-~*' * 4)
for c in range(1, 11):
    print(f'\033[36m{num} x {c :>2} = {num * c}\033[m')
print('\033[35m*~-' * 4)
# corrigido
