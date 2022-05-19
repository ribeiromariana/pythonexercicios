print('\033[31mDigite 999 para encerrar o programa.\033[m')
num = int(input('Digite um número inteiro: '))
total = 1
soma = num
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        total += 1
        soma += num
print(f'Foram digitados {total} números e o total da soma deles é de {soma}!')
