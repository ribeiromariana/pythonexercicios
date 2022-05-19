print('\033[35m-*~' * 7)
print('SEQUÊNCIA DE FIBONACCI')
print('-*' * 11)
n = int(input('\033[33mQuantos termos você quer? \033[m'))
t1 = 0
t2 = 1
print('\033[32m-=*~*' * n)
print(f'\033[36m{t1} → {t2} → ', end='')
total = 3
while total <= n:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    total += 1
print('FIM')
print('\033[32m-=*~*' * n)
# corrigido
