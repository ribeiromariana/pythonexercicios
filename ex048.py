soma = 0
quantidade = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        quantidade += 1
print(f'A soma de todos os {quantidade} númers impares divisíveis por 3 é de: \033[35m{soma}\033[m!')
# corrigido
