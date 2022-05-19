dados = list()
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer adicionar mais alunos? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('Boletim dos alunos: ')
print(f'nº {"nome":<12} {"média":^7}')
for p, a in enumerate(dados):
    print(f'{p}  {a[0]:<12} {a[2]:^7.1f}')
while True:
    num_a = int(input('Mostrar notas de qual aluno? \033[31m[999 para parar] \033[m'))
    while num_a > len(dados) - 1 and num_a != 999:
        num_a = int(input('Digite o número do aluno que você quer ver as notas: \033[31m[999 para parar]\033[m '))
    if num_a == 999:
        break
    print(f'Notas de {dados[num_a][0]}: {dados[num_a][1]}')
print('=-' * 20)
print('Programa encerrado, volte sempre! :)')
