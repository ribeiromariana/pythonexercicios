from time import sleep


def maior(*nums):
    print('Analizando os valores...')
    sleep(0.5)
    m = cont = 0
    for n in nums:
        print(n, end=' ')
        sleep(0.5)
        if cont == 0:
            m = n
        elif n > m:
            m = n
        cont += 1
    print(f'Foram passados \033[32m{cont} valores ao todo.\033[m')
    print(f'O maior número entre \033[36m{nums}\033[m é \033[35m{m}\033[m!')
    print('¬¬' * 22)


# Programa principal
maior(7, 6, 3, 9, 2)
maior(4, 6, 2, 0)
maior(3)
maior(23, 54, 12, 9)
maior()
