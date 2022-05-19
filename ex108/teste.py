import moeda

num = float(input('Quantos reais? R$'))
print('¬¬'  * 25)
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}!')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}!')
print(f'Aumentando 10%, {moeda.moeda(num)} passa a ser {moeda.moeda(moeda.aumentar(num, 10))}!')
print('¬¬' * 25)
