dias = int(input('Por \033[1;33mquantos dias\033[m o carro foi alugado? '))
km = float(input('\033[1;32mQuantos km\033[m foram percorridos? Km:'))
valor = (60 * dias) + (km * 0.15)
print(f'O \033[34mvalor total\033[m a pagar é \033[36mR${valor:.2f}\033[m.')
