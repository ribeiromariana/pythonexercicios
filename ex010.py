carteira = float(input('\033[31mQuantos reais tem-se na carteira? R$'))
dolar = carteira / 4.97
print(f'\033[mCom \033[4;32mR${carteira:.2f}\033[m, você pode comprar \033[4;35mUS${dolar:.2f}\033[m!')
