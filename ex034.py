salario = float(input('Digite o seu salário, para saber qual será o seu aumento: R$'))
# Calculando o aumento e a sua porcentagem, respectivamente.
if salario > 1250.00:
    aumento = [(salario + salario * 10 / 100), 10]
else:
    aumento = [(salario + salario * 15 / 100), 15]
print(f'O salário de R${salario:.2f}, passa a ser R${aumento[0]:.2f}, com um aumento de {aumento[1]}%!')
