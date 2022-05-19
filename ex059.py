from time import sleep
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
menu = '''\033[35m[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
\033[34mSua escolha:\033[m '''
opcao = int(input(menu))
maior = 0
while opcao != 5:
    if opcao == 1:
        print(f'A soma dos valores escolhidos é igual a {num1 + num2}.')
    elif opcao == 2:
        print(f'O produto dos valores escolhidos é igual a {num1 * num2:.2f}.')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        else:
            maior = num1
        print(f'O maior número digitado foi: {maior}')
    elif opcao == 4:
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
    else:
        print('\033[31mValor inválido. Tente novamente.\033[m')
    sleep(1.5)
    opcao = int(input(menu))
