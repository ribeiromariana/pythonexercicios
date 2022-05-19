valor_casa = float(input('\033[35mValor da casa: R$\033[m'))
salario = float(input('\033[33mSalário do comprador: R$\033[m'))
anos = int(input('\033[34mEm quantos anos você vai pagar? \033[m'))
valor_pm = valor_casa / (anos * 12)
print(f'Para pagar uma casa de \033[35mR${valor_casa:.2f}\033[m em \033[34m{anos} anos\033[m, a prestação será de'
      f'\033[31mR${valor_pm:.2f}')
if valor_pm > (salario * 30 / 100):
    print('\033[31mEmpréstimo NEGADO.')
else:
    print(f'\033[32mEmpréstimo ACEITO!')
# corrigido
