preco = float(input('\033[33mPreço do produto: R$\033[m'))
desc = preco - (preco * 5 / 100)
print(f'O produto que custava \033[33mR${preco}\033[m, agora na \033[1;35mpromoção de 5%\033[m, está custando \033[35m'
      f'R${desc:.2f}\033[m, \033[31mAPROVEITE!')
