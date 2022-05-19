from random import randint
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
resultado = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f'{" Ranking ":¬^37}')
for i, v in enumerate(resultado):
    print(f' {i + 1}º colocado: {v[0]} com {v[1]} pontos')
