dados = {}
dados['nome'] = str(input('Nome: ')).title().strip()
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] > 7:
    dados['resultado'] = 'Aprovado (a)'
elif dados['media'] > 5:
    dados['resultado'] = 'Recuperação'
else:
    dados['resultado'] = 'Reprovado (a)'
print('+-+' * 16)
for key, value in dados.items():
    print(f'     - {key} é igual a {value}')

## Antigo -V *Depois de 24 dias sem programar :O
'''aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] > 7:
    aluno['situaçao'] = 'Aprovado'
elif aluno['media'] > 6:
    aluno['situaçao'] = 'Recuperação'
else:
    aluno['situaçao'] = 'Reprovado'
print(' __' * 12)
for k, v in aluno.items():
    print(f'    - {k} é igual a {v}')'''