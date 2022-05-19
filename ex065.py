teste = 'S'
total = soma = menor = maior = 0
while teste == 'S':
    num = int(input('\033[35mDigite um número inteiro: '))
    total += 1
    if total == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    teste = str(input('\033[33mQuer continuar? [S/N]: \033[m')).upper()
media = soma / total
if teste == 'N':
    print(f'\033[36mA média dos números digitados acima é de {media:.1f}.')
    print(f'\033[32mO MAIOR número foi {maior} \033[34me o MENOR foi {menor}.\033[m')
elif teste != 'S':
    print('\033[31mAlgo de errado aconteceu. Tente novamente\033[m')
