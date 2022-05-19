print(f'{" Analizando uma Matriz ":=^33}')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares_s = soma_tc = maior = 0
for c in range(0, 3):
    for f in range(0, 3):
        valor = int(input(f'Digite um valor para [{c}, {f}]: '))
        matriz[c][f] = valor
        if valor % 2 == 0:
            pares_s += valor
        if c == 1:
            if f == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor
print('¬.' * 15)
for l in matriz:
    soma_tc += l[2]
    for n in l:
        print(f'[{n:^5}]', end=' ')
    print()
print(f'\033[35mA soma de todos os valores pares digitados é de {pares_s}')
print(f'\033[34mA soma dos valores da terceira coluna é de {soma_tc}')
print(f'\033[32mO maior valor da segunda linha é {maior}')
