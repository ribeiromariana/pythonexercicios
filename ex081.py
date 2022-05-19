lista = []
while True:
    lista.append(int(input('Digite o número que quer adicionar: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-' * 20)
print(f'Os números adicionados foram: {lista}')
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Em ordem decrescente: {lista}')
if lista.count(5) > 0:
    print('O valor 5 está na lista')
else:
    print('O número 5 NÃO está na lista.')
