from ex115.menu import validandodados
from ex115.menu.arquivo import *
def linha(txt):
    tam = 40
    print('¬' * tam)
    print(f'{txt:^{tam}}')
    print('¬' * tam)


def menu(lista):
    while True:
        linha('Menu Principal')
        for i, v in enumerate(lista):
            print(f'    \033[35m{i+1}- \033[34m{v}\033[m')
        print('¬' * 40)
        valor = validandodados.validar('Sua opção: ', 1, 2, 3, 4)
        submenu(valor)
        if valor == 3:
            break


def submenu(num):
    from time import sleep
    if num == 1:
        linha('Pessoas cadastradas: ')
        lerarquivo('pessoas.txt')
    elif num == 2:
        linha('Cadastrar nova pessoa')
        nm = str(input('Nome: ')).strip().title()
        anos = int(input('Idade: '))
        organizararq('pessoas.txt', nm, anos)
    elif num == 3:
        print('\033[31mEncerrando programa...\033[m')
        sleep(0.4)
        linha('Volte sempre :)')
    elif num == 4:
        resetararq('pessoas.txt')
