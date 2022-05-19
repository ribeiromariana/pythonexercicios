pessoa = dict()
grupo = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro!! Digite apenas S ou N.')
    if resp == 'N':
        break
    print('´`' * 25)

pessoas_q = len(grupo)
print('¬¬' * 25)
print(f'    - {pessoas_q} pessoas foram cadastradas.')

idades = 0
mulheres = []
for i, v in enumerate(grupo):
    idades += v['idade']
    if v['sexo'] == 'F':
        mulheres.append(v['nome'])
media = idades / pessoas_q

print(f'    - Média de idade: {media:.2f}')
print(f'    - Mulheres cadastradas: {mulheres[:]}')
print('    - Pessoas com idade acima da média: ')
for ii, vv in enumerate(grupo):
    if vv['idade'] > media:
        print(f'        => Nome: {vv["nome"]}; Idade: {vv["idade"]}; Sexo: {vv["sexo"]}')
