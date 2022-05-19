def leiadinheiro(txt):
    valid = False
    while not valid:
        valor = str(input(txt)).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            valid = False
            print(f'\033[0;31mO valor \'{valor}\' não é um preço. Tente novamente.\033[m')
        else:
            return float(valor)


def leiaint(perg):
    while True:
        valor = input(perg)
        if not valor.isnumeric():
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            return valor
