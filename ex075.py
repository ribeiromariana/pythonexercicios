num = (
int(input('Digite um número: ')), int(input('Mais um número: ')), int(input('Mais um: ')), int(input('Mais um: ')))
print(num)
print(f'\033[35mO número 9 apareceu {num.count(9)} vezes')
if num.count(3) >= 1:
    print(f'\033[33mO número 3 foi digitado na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print(f'\033[34mOs números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
