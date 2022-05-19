from random import randint
from time import sleep
num_pc = randint(0, 5)
nome = str(input('Digite o seu nome para começar: ')).strip()
num_player = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...\nSerá que você vai me vencer??')
sleep(3)
if num_player == num_pc:
    print('Muito bem, você VENCEU! \nO que acha de jogar mais uma vez?')
else:
    print(f'Você PERDEU, eu escolhi o número {num_pc} e não o número {num_player}! \nBoa sorte na próxima!')
print(f'Fim de jogo.\nFoi bom jogar com você, {nome.title()}! Estou te esperando para a próxima rodada!!')
# corrigido
