def moeda(valor=0, simb='R$'):
    return f'{simb}{valor:.2f}'.replace('.', ',')


def dobro(n=0, moe=False):
    """
    Serve para calcular o dobro de um valor monetário
    :param n: preço recebido
    :param moe: se quer ou não a formatação monetária
    :return: retorna o dobro do preço, formatado ou não
    """
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


def linha(txt=''):
    tam = len(txt) + 16
    print('-' * tam)
    print(f'        {txt}')
    print('-' * tam)


def resumo(valor=0, aum=10, dim=20):
    linha('Resumo Do Valor')
    print(f'Preço analizado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aum}% de aumento: \t{aumentar(valor, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(valor, dim, True)}')
    print('¬' * 31)


help(dobro)
