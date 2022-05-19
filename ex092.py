# 35 anos de colaboração
from datetime import date
nome = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
CTPS = int(input('Número da carteira de trabalho (0 se não tem): '))
idade = date.today().year - nascimento
dados = {'Nome': nome,
         'Idade': idade,
         'CTPS': CTPS}

if CTPS != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salãrio: R$'))
    dados['Idade para se aposentar'] = (dados['Ano de contratação'] + 35) - nascimento

print('´´' * 20)
for k, v in dados.items():
    print(f'    - {k} é {v}')
