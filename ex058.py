from random import randint
pc = randint(0, 10)
print('\033[33m*~-' * 4, '\033[36mEscolha entre 0 e 10!', '\033[33m-~*\033[m' * 4)
player = int(input('\033[35mDigite qual número que você acha que o pc pensou: '))
tentativas = 1
while player != pc:
    player = int(input('\033[31mERROU! \033[35mTente novamente: '))
    tentativas += 1
print(f'\033[32mEm {tentativas} tentativas, você acertou. Muuuito bem!')
