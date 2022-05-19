print('\033[34m*~- DIGITE SEUS DADOS PARA SE CADASTRAR -~*')
maiores = homens = meninas = 0
while True:
    idade = int(input('\033[33mDigite a sua idade:\033[m '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[35mDigite o seu sexo [M/F]: \033[m')).upper().strip()[0]
    if idade > 18:
        maiores += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        meninas += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('\033[32mQuer continuar? [S/N]:\033[m ')).upper().strip()[0]
    if cont in 'N':
        break
print(f'\033[36m{maiores} pessoas são maiores de 18 anos. \n{homens} homens foram cadastrados.')
print(f'{meninas} mulheres têm menos de 20 anos.')
print('\033[31mPrograma finalizado.\033[m')
