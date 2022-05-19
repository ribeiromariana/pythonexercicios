h = float(input('\033[33mQual é a altura da parede? m:'))
l = float(input('\033[34mQual é a largura da parede? m:\033[m'))
a = l * h
qtdd_latas = a / 2
print(f'Sua parede tem dimensão de \033[32m{h}x{l}\033[m e a sua \033[4;35márea\033[m é de \033[35m{a:.1f}m²\033[m. '
      f'\nPara \033[31mpintar essa parede\033[m, você precisará de \033[31m{qtdd_latas:.2f}l de tinta\033[m!!')
