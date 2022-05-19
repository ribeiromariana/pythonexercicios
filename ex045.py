from random import choice
from time import sleep
print(f'\033[33m{" Jokêmpo ":=^36}\033[m')
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
player = str(input('Escolha \033[36mpedra\033[m, \033[35mpapel\033[m ou \033[32mtesoura\033[m: ')).strip().lower()
print('JO')
sleep(0.7)
print('KEM')
sleep(0.7)
print('POO!!!')
if pc == 'pedra':
    if player == 'pedra':
        print(f'\033[33mEMPATE!\033[m Você e o computador escolheram \033[36m{pc}\033[m!')
    elif player == 'papel':
        print(f'\033[32mVOCÊ GANHOU!\033[m O computador escolheu \033[36m{pc}\033[m!')
    elif player == 'tesoura':
        print(f'\033[31mPERDEU!\033[m O computador escolheu \033[36m{pc}\033[m!')
    else:
        print('\033[1;31mOpção inválida. Tente novamente.\033[m')
elif pc == 'papel':
    if player == 'pedra':
        print(f'\033[31mPERDEU!\033[m O computador escolheu \033[35m{pc}\033[m!')
    elif player == 'papel':
        print(f'\033[33mEMPATE!\033[m Você e o computador escolheram \033[35m{pc}\033[m!')
    elif player == 'tesoura':
        print(f'\033[32mVOCÊ GANHOU!\033[m O computador escolheu \033[35m{pc}\033[m!')
    else:
        print('\033[1;31mOpção inválida. Tente novamente.\033[m')
else:
    if player == 'pedra':
        print(f'\033[32mVOCÊ GANHOU!\033[m O computador escolheu \033[32m{pc}\033[m!')
    elif player == 'papel':
        print(f'\033[31mPERDEU!\033[m O computador escolheu \033[32m{pc}\033[m!')
    elif player == 'tesoura':
        print(f'\033[33mEMPATE!\033[m Você e o computador escolheram \033[32m{pc}\033[m!')
    else:
        print('\033[1;31mOpção inválida. Tente novamente.\033[m')
