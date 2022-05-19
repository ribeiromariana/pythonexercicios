from random import randint
vitorias = 0
print('-~*' * 3, 'Jogo do PAR ou ÍMPAR', '*~-' * 3)
while True:
    pc = randint(0, 10)
    print()
    escolha = str(input('\033[33mVocê vai ser par ou impar? [P/I]: ')).upper().strip()[0]
    while escolha not in 'PIÍ':
        escolha = str(input('\033[31mO valor digitado é inválido. Tente novamente: \033[m')). upper().strip()[0]
    print('- ' * 14)
    jogador = int(input('\033[34mDigite o seu número: \033[m'))
    print('\033[35m_ ' * 12)
    soma = pc + jogador
    print(f'      {pc} + {jogador} = {soma}!')
    print('- ' * 12, '\033[m')
    if soma % 2 == 0:
        if escolha in 'P':
            vitorias += 1
            print('Logo, \033[32mvocê venceu!\033[m')
        elif escolha in 'IÍ':
            print(f'\033[34mVocê perdeu com {vitorias} vitórias consecutivas.\033[m')
            break
    elif soma % 2 != 0:
        if escolha in 'IÍ':
            vitorias += 1
            print('\033[32mVocê venceu! \033[35mBela jogada!\033[m')
        elif escolha in 'P':
            print(f'\033[34mVocê perdeu com {vitorias} vitórias consecutivas.\033[m')
            break
print('Foi um ótimo jogo. O que acha de jogar de novo?')
