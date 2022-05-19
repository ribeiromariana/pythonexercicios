dados = []
pessoas = ['Fora Bozo lixo', 13]
pesadas = []
leves = []
while True:
    pessoas[0] = str(input('Nome: ')).title()
    pessoas[1] = float(input('Peso: kg'))
    dados.append(pessoas[:])
    resp = str(input('Quer continuar? ')).upper().strip()[0]
    print('-¬' * 20)
    if resp == 'N':
        break
maior = menor = dados[0][1]
for p in dados:
    if p[1] < menor:
        menor = p[1]
    elif p[1] > maior:
        maior = p[1]

for ps in dados:
    if maior in ps:
        pesadas.append(ps[0])
    elif menor in ps:
        leves.append(ps[0])
dados.append(pesadas[:])
dados.append(leves[:])
print(f'Foram cadastradas {len(dados) - 2} pessoas.')
print(f'O maior peso foi {maior}kg, peso de {dados[-2]}')
print(f'O menor peso foi {menor}kg, peso de {dados[-1]}')
# N ERA PRA ADICIONAR AS PESADAS E LEVES NA LISTA, MAS DEU CERTO!