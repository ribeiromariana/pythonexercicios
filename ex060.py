num = int(input('Digite um número: '))
x = num - 1
total = num * x
while x != 0:
    x -= 1
    if x != 0:
        total = total * x
print(f'{num}! = {total}')

n = int(input('Digite um número para calcular o seu fatorial: '))
f = 1
for c in range(n, 0, -1):
    f *= c
print(f'O fatorial de {n} é {f}.')
