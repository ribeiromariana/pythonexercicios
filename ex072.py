extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    while 0 > num or num > 20:
        num = int(input('Algo de errado aconteceu. Tente novamente: '))
    print(f'O número digitado foi o \033[35m{extenso[num]}\033[m')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('\033[33mPrograma finalizado. Volte sempre!')
