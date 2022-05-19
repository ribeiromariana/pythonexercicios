n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
# Analizando o maior e os menores
maior = n1
menores = [n2, n3]
if n2 > n1 and n2 > n3:
    maior = n2
    menores = [n1, n3]
else:
    maior = n3
    menores = [n1, n2]
# Analizando qual dos menores é o menor
menor = menores[0]
if menores[1] < menores[0]:
    menor = menores[1]
print(f'O MAIOR número é: {maior} \nO MENOR número é: {menor}')
# Corrigido
