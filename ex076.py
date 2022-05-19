produtos = ('Batata', 4, 'Café', 11.57, 'Carne', 34.71, 'Arroz', 20, 'Bolacha', 1.49, 'Pão de Forma', 15.59)
# print(produtos)
print('-' * 50)
print(f'{"Lista de Preços":^50}')
print('-' * 50)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<40}', end='')
    else:
        print(f'R${produtos[c]:>7.2f}')
print('-' * 50)
# tive q olhar a resposta para entender a solução