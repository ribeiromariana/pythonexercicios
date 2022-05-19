valor = int(input('Qual valor inteiro vai ser sacado? R$'))
nota50 = nota20 = nota10 = nota1 = 0
while True:
    while valor >= 50:
        valor -= 50
        nota50 += 1
    while valor >= 20:
        valor -= 20
        nota20 += 1
    while valor >= 10:
        valor -= 10
        nota10 += 1
    while valor >= 1:
        valor -= 1
        nota1 += 1
    if valor == 0:
        break
print('Serão entregues:')
if nota50 > 0:
    print(f'\033[33m{nota50} notas de R$50')
if nota20 > 0:
    print(f'\033[34m{nota20} notas de R$20')
if nota10 > 0:
    print(f'\033[35m{nota10} notas de R$10')
if nota1 > 0:
    print(f'\033[32m{nota1} notas de R$1 ')
print('\033[mFim')
