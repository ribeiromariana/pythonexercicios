cor = {'ciano': '\033[36m',
       'roxo': '\033[35m',
       'limpa': '\033[m',
       'amarelo': '\033[33m'}
num1 = int(input(f'{cor["ciano"]}Digite um valor: '))
num2 = int(input(f'{cor["roxo"]}Digite outro valor:{cor["limpa"]} '))
result = num1 + num2
print(f'A soma entre {cor["ciano"]}{num1}{cor["limpa"]} e {cor["roxo"]}{num2}{cor["limpa"]} é igual a: {cor["amarelo"]}'
      f'{result}{cor["limpa"]}!!')
