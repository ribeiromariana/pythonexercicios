# from ex115.menu import interface

def validar(msg, *ops):
    while True:
        try:
            valor = int(input(msg))
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não informar os dados\033[m')
        except:
            print('\033[31mErro! Digite um número inteiro.\033[m')
        else:
            if valor in ops:
                return valor
            else:
                print(f'\033[93mPor favor, digite um valor entre {ops[0]} e {ops[-1]}!\033[m')
