soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('\033[36mDigite um número inteiro: \033[m'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'\033[33mO resultado da soma dos {cont} números PARES digitados acima foi de: \033[35m{soma}\033[33m!!')
