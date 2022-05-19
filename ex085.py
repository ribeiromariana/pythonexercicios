nums = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}ª valor: '))
    if valor % 2 == 0:
        nums[0].append(valor)
    else:
        nums[1].append(valor)
print('¬-' * 30)
nums[0].sort()
print(f'\033[34mValores pares em ordem crescente: {nums[0]}')
nums[1].sort()
print(f'\033[35mValores impares em ordem crescente: {nums[1]}')
