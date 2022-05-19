n1 = int(input('\033[32mDigite o primeiro número: \033[m'))
n2 = int(input('\033[33mDigite o segundo número: \033[m'))
if n1 > n2:
    print('\033[35mO \033[1mprimeiro número\033[0;35m é o maior!!')
elif n1 < n2:
    print('\033[36mO \033[1msegundo número\033[0;36m é o maior!!')
else:
    print('\033[1;31mNão\033[0;31m existe valor maior, os dois são iguais!\033[m')
# corrigido
