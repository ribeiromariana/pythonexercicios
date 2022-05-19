def leiaint(msg):
    valid = False
    while not valid:
        try:
            entrada = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mTivemos um erro com os dados informados!\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não digitar os dados.\033[m')
            break
        else:
            return entrada


def leiafloat(txt):
    while True:
        try:
            valor = float(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mTivemos um erro com os dados informados.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados.\033[m')
            break
        else:
            return valor


inteiro = leiaint('Digite um número INTEIRO: ')
real = leiafloat('Digite um número REAL: ')
print(f'O número inteiro informado foi {inteiro} e o real foi {real}!')
