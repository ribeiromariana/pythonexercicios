print(f'{" Criando uma matriz ":¬^33}')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]# 1ª linha, 2ª e 3ª

for c in range(0, 3):
    for f in range(0, 3):
        matriz[c][f] = int(input(f'Digite um valor para [{c}, {f}] '))

for l in matriz:
    for n in l:
        print(f'[{n:^5}]', end=' ')
    print()
