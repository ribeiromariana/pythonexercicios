print('\033[32m*~- Lojinha da Vovó -~*\033[m')
total = maisd1000 = maisB = 0
nome_maisB = ' '
while True:
    print('=' * 20)
    nome = str(input('\033[35mNome do produto: '))
    preco = float(input('\033[34mPreço do produto: R$\033[m'))
    print('=' * 20)
    if total == 0:
        maisB = preco
    if preco < maisB:
        maisB = preco
        nome_maisB = nome
    total += preco
    if preco > 1000:
        maisd1000 += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('\033[33mQuer continuar? [S/N]: \033[m')).strip().upper()[0]
    if cont == 'N':
        break
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'{maisd1000} produtos custam mais de R$1000.')
print(f'{nome_maisB} foi o produto mais barato, custando R${maisB}')
print('Programa finalizaado')
