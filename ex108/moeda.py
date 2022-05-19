def dobro(n=0):
    n *= 2
    return n


def metade(n=0):
    n /= 2
    return n


def aumentar(n=0, p=0):
    n = n + n * p / 100
    return n


def diminuir(n=0, p=0):
    n -= n * p / 100


def moeda(valor=0, simb='R$'):
    return f'{simb}{valor:.2f}'.replace('.', ',')
