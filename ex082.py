num = []
while True:
    num.append(int(input('Digite o valor que quer adicionar: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-' * 20)
print(f'Os números digitados foram: {num}')
par = []
impar = []
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Lista de pares: {par}')
print(f'Lista de ímpares: {impar}')
