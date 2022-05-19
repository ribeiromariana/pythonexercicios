from datetime import date
menores = 0
maiores = 0
for c in range(0, 7):
    data_nasc = int(input('Ano de nascimento: '))
    idade = date.today().year - data_nasc
    # print(f'Então a sua idade é {idade}!')
    if idade < 21:
        menores = menores + 1
    else:
        maiores = maiores + 1
print(f'\033[35m{menores} pessoas são MENORES de idade\033[m; e \033[34m\n{maiores} pessoas são MAIORES de idade.\033[m')
# corrigido
