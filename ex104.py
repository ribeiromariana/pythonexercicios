def leiaint(perg):
    while True:
        valor = input(perg)
        if not valor.isnumeric():
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            return valor


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}!')
