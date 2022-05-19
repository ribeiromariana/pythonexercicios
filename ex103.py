def ficha(nome = '', gols = ''):
    if not gols.isnumeric():
        gols = 0
    if nome == '':
        nome = '<não informado>'
    print(f'O jogador {nome.title()} fez {gols} gol(s) no campeonato.')


n = str(input('Nome: '))
g = input('Gols: ')
ficha(n, g)