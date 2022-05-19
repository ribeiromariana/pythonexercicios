m = float(input('Escreva um valor em \033[4;97mmetros\033[m: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'\033[97m{m:.2f}m\033[m equivale a: \n\033[31m{km:.2f}km\033[m; \n\033[32m{hm:.2f}hm\033[m;')
print(f'\033[33m{dam:.2f}dam\033[m; \n\033[34m{dm:.2f}dm\033[m; \n\033[35m{cm:.2f}cm\033[m; \n\033[36m{mm:.2f}mm')
