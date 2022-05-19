total = soma = 0
while True:
    num = int(input('Digite um número \033[31m(999 para parar)\033[m: '))
    if num == 999:
        break
    total += 1
    soma += num
print(f'\033[35mForam digitados {total} números. A soma entre eles é de {soma}.')
