idades = 0
homem_velho = 'Indefinido'
idade_hv = 0
mulheres_menos = 0
for c in range(0, 4):
    nome = str(input('\033[36mDigite o seu nome: '))
    idade = int(input('\033[33mDigite a sua idade: \033[31m'))
    sexo = int(input('Digite 1 ou 2 de acordo as informações abaixo: \n\033[35m[1] Mulher \n\033[34m[2] Homem\033[m \nVocê é Homem ou Mulher?'))
    if sexo == 1 and idade > 20:
        mulheres_menos = mulheres_menos + 1
    if sexo == 2 and idade > idade_hv:
        idade_hv = idade
        homem_velho = nome
    if sexo == 1:
        sexo = 'mulher'
    elif sexo == 2:
        sexo = 'homem'
    else:
        print('Número inválido. Tente novamente.')
    idades = idade + idades
print(f'\033[32mA média de idade do grupo é de {idades / 4:.0f}!')
print(f'\033[34mO homem mais velho do grupo se chama {homem_velho}.')
print(f'\033[35mE {mulheres_menos} mulheres têm menos de 20 anos.')
