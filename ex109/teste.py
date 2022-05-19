import moeda

num = float(input('Quantos reais? R$'))

print('¬¬' * 25)

print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, moe=True)}!')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, moe=True)}!')

print(f'Aumentando 10%, {moeda.moeda(num)} passa a ser {moeda.aumentar(num, 10, moe=True)}!')
print(f'Diminuindo 34%, temos {moeda.diminuir(num, 34, moe=True)}')

print('¬¬' * 25)
