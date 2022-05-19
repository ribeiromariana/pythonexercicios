'''from random import randint as qlq
a1 = input('Escreva o nome de um aluno: ')
a2 = input('Escreva o nome de outro aluno: ')
a3 = input('Escreva o nome de outro aluno: ')
a4 = input('Escreva o nome de outro aluno: ')
s = qlq(1,4)
if s == 1:
    print(f'O aluno escolhido foi {a1}.')
elif s == 2:
    print(f'O aluno escolhido foi {a2}.')
elif s == 3:
    print(f'O aluno escolhido foi {a3}.')
else:
    print(f'O aluno escolhido foi {a4}.')'''
from random import choice
a1 = input('1º aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'O(a) alunx escolhidx foi: {escolhido}!')
#CORRIGIDO
