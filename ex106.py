# Data: 10/12/2021 - 15:30


def linha(texto, cor):
    print(f'\033[{cor}m', end='')
    print('¬' * (len(texto) + 4))
    print(f'  {texto}')
    print('-' * (len(texto) + 4))
    print(f'\033[m', end='')


def busca(nome):
    from time import sleep
    linha(f"Acessando o manual do comando '{nome}'", 93)
    sleep(0.3)
    print(f'\033[35m', end='')
    help(nome)
    print(f'\033[m', end='')


# Programa Principal
while True:
    linha('Sistema de ajuda PyHelp', 36)
    resp = str(input('Função ou biblioteca > ')).strip()
    if resp.upper() == 'FIM':
        linha('Até logo!', 31)
        break
    else:
        busca(resp)
