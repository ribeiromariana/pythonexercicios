p = {'d': '\033[4;31mdobro\033[m', 't': '\033[4;33mtriplo\033[m', 'rq': '\033[4;36mraiz quadrada\033[m'}
n = int(input(f'\033[35mDigite um número para saber o seu {p["d"]}\033[35m, {p["t"]}\033[35m e {p["rq"]}\033[35m: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print(f'\033[mO {p["d"]} de \033[35m{n}\033[m é \033[31m{d}\033[m.')
print(f'O {p["t"]} de \033[35m{n}\033[m é \033[33m{t}\033[m.')
print(f'A {p["rq"]} de \033[35m{n}\033[m é \033[36m{rq:.2f}\033[m.')
