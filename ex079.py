valores = []
while True:
    num = int(input('\033[35mDigite um valor: '))
    if num in valores:
        print(f'\033[31mNúmero repitido. Não adicionei')
    else:
        valores.append(num)
        print(f'\033[32mNúmero adicionado com sucesso!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[36mQuer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'\033[33mOs valores digitados foram: {sorted(valores)}')
