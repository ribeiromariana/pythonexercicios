def moeda(valor=0, simb='R$'):
    return f'{simb}{valor:.2f}'.replace('.', ',')


def dobro(n=0, moe=False):
    n *= 2
    if moe:
        n1 = moeda(n)
        return n1
    else:
        return n


def metade(n=0, moe=False):
    n /= 2
    if moe:
        n1 = moeda(n)
        return n1
    else:
        return n


def aumentar(n=0, p=0, moe=False):
    n = n + n * p / 100
    if moe:
        n1 = moeda(n)
        return n1
    else:
        return n


def diminuir(n=0, p=0, moe=False):
    n -= n * p / 100
    if moe:
        n1 = moeda(n)
        return n1
    else:
        return n
