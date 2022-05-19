num = int(input('Digite um número inteiro: '))
print('''Escolha qual será a base de conversão:
[ 1 ] Binário;
[ 2 ] Octal;
[ 3 ] Hexadecimal.''')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print(f'O número {num} em Binário fica: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} em Octal fica: {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} em Hexadecimal fica: {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
# corrigido
