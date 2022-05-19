from random import randint


def sorteia(lista):
    lista.clear()
    for c in range(0, 5):
        lista.append(randint(0, 9))
    print(f'Os 5 números sorteados foram: \033[35m{lista}\033[m!')
    print('¬¬' * 23)


def soma_par(lista):
    soma = 0
    print(f'Os valores pares são:\033[94m ', end='')
    for v in lista:
        if v % 2 == 0:
            print(v, end=' ')
            soma += v
    print(f'\n\033[mE a soma deles é igual a \033[32m{soma}\033[m!')
    print('¬¬' * 23)


nums = list()
sorteia(nums)
soma_par(nums)
