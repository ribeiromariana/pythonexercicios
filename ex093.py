jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

gols = list()
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols foram feitos na partida {c}? ')))

total = sum(gols)
jogador['Gols'] = gols[:]
jogador['Total'] = total

print('¬¬' * 30)
print(jogador)
print('´`' * 30)

for k, v in jogador.items():
    print(f'        - {k} é igual a {v}')
print('´`' * 30)

print(f'O atleta {jogador["Nome"]} jogou {partidas} partidas.')

for i, v in enumerate(jogador['Gols']):
    print(f'    => Na {i + 1}ª partida, fez {v} gols')
    
print(f'Foi um total de {jogador["Total"]} gols.')
