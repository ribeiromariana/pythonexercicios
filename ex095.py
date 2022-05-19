jogador = dict()
gols = list()
time = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome: ')).title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'    Gols da partida {c}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N!')
    if resp == 'N':
             break
    print('~-' * 22)
print(time)
print(f'{"Cod"} ', end='')
for i in time[0]:
    print(f'{i:<15}', end='')
print()
print('--' * 23)

for i, v in enumerate(time):
    print(f'{i:^3} ', end='')
    for d in v.values():
        print(f'{str(d):<14}', end='')
    print()
valores = []
while True:
    resp = int(input('Qual jogador você que analizar? (999 para parar) '))
    if resp == 999:
        break
    for i, v in enumerate(time):
        if resp == i:
            print('--' * 22)
            print(f'    => O membro {v["nome"]}, jogou {len(v["gols"])} partidas e fez um total de {v["total"]} gols. ')
        valores.append(i)
    if resp not in valores[:]:
        print(f'    *Erro! O jogador de código {resp} não existe. Tente novamente.')
