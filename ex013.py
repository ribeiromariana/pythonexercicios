s = float(input('\033[34mSalário: R$\033[m'))
aumento = s + (s * 15 / 100)
print(f'O salário que era \033[34mR${s:.2f}\033[m, agora com o \033[31maumento\033[m de 15%, é \033[31mR${aumento:.2f}')

produto = float(input('\033[33mQual é o preço do produto? R$\033[m'))
a_vista = produto - (produto * 10 / 100)
parcelado = produto + (produto * 5 / 100)
print(f'O preço do produto à vista é \033[35mR${a_vista:.2f}\033[m. \nParcelado, com juros, é \033[34mR${parcelado:.2f}'
      f'\033[m, ou seja, um aumento de \033[36mR${produto * 5 / 100:.2f}\033[m!')
