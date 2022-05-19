from time import sleep
vezes = 0
num = int(input('Digite um número inteiro: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', c, end=' ')
        vezes += 1
    else:
        print('\033[31m', c, end=' ')
    sleep(0.1)
if vezes == 2:
    print(f'\n\033[mO número {num} É PRIMO!')
elif vezes > 2:
    print(f'\n\033[mO número {num} NÃO é PRIMO!')
