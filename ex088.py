from random import randint
from time import sleep
print(f'{" Gerador de Palpites da Mega Sena! ":=^45}')
jogos = []
palpites = []
quant = int(input('Quantos palpites você quer? '))
for palp in range(0, quant):
    for c in range(0, 6):
        num = randint(1, 60)
        while num in palpites:
            num = randint(1, 60)
        palpites.append(num)
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
print(f"{f' Sorteando {quant} jogos ':.^35}")
for c in range(1, quant + 1):
    print(f'Jogo {c}: {jogos[c - 1]}')
    sleep(1)
