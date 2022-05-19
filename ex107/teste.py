import moeda

num = float(input('Quantos reais? R$'))
print(f'A metade de R${num} é R${moeda.metade(num)}!')
print(f'O dobro de R${num} é R${moeda.dobro(num)}!')
print(f'Aumentando 10%, R${num} passa a ser R${moeda.aumentar(num, 10)}!')

