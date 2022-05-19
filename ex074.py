from random import randint
num = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
total = maior = menor = 0
for n in num:
    total += 1
    if total == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    print(n, end=' ')
print(f'\n\033[34mO MENOR número foi {menor}. \n\033[35mO MAIOR foi {maior}')
# Ou para ver o maior/menor, fazer assim: max(num) ou min(num)
