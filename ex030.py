from time import sleep
num = str(input('Digite um número inteiro: '))
ult = int(num[len(num) - 1])
teste = ult == 0 or ult == 2 or ult == 4 or ult == 6 or ult == 8
print('PROCESSANDO...')
sleep(1)
if teste is True:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é impar!')
# Corrigido