def fatorial(num, show = False):
    """
    Serve para calcular o fatorial do valor escolhido
    :param num: número que será calculado o fatorial
    :param show: caso for verdadeiro, a função vai mostrar a conta para encontrar o fatorial, se não, não mostrará
    :return: retorna o resultado da conta, mostrando ou não o processo do cálculo
    04/12/2021
    """
    from time import sleep
    fac = num
    print(f'O fatorial de {num} é...')
    sleep(0.5)
    if show:
        print(f'{num} x', end=' ')
    for c in range(num - 1, 0, -1):
        fac *= c
        if show:
            if c == 1:
                print(f'{c} =', end=' ')
            else:
                print(f'{c} x', end=' ')
    print(fac)
    print('¬¬' * 30)


# Programa principal
f = 5
fatorial(f, True)
help(fatorial)
