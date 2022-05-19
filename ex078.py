nums = []
for c in range(0, 5):
    nums.append(int(input(f'Digite um número para a posição {c}: ')))
print('==' * 22)
print(f'Os números digitados foram {nums}')
maior = menor = 0
pos_maior = [0]
pos_menor = [0]
for p, n in enumerate(nums):
    if p == 0:
        maior = menor = n
        if p != 0:
            pos_menor.insert(0, p)
            pos_maior.insert(0, p)
    else:
        if n == maior:
            pos_maior.append(p)
        if n == menor:
            pos_menor.append(p)
        if n > maior:
            maior = n
            pos_maior.clear()
            pos_maior.append(p)
        if n < menor:
            menor = n
            pos_menor.clear()
            pos_menor.append(p)
print(f'O maior valor foi {maior} nas posições ', end='')
for p in pos_maior:
    print(p, end='... ')
print(f'\nO menor valor foi {menor} nas posições ', end='')
for p in pos_menor:
    print(p, end='... ')
# Poderia ter feito assim:
# Ler a lista com o enumerate e depois ver as possições do maior e menor num, assim a solução ficaria menor