from datetime import date
ano_nascimento = int(input('Digite o seu ano de nascimento para saber a sua categoria: '))
idade = date.today().year - ano_nascimento
print(f'\033[32mO atleta tem {idade} anos.\033[m')
if idade <= 9:
    categoria = '\033[35mMIRIM'
elif idade <= 14:
    categoria = '\033[33mINFANTIL'
elif idade <= 19:
    categoria = '\033[36mJUNIOR'
elif idade <= 25:
    categoria = '\033[97mSÊNIOR'
else:
    categoria = '\033[31mMASTER'
print(f'\033[32mE sua categoria é: {categoria}')
# corrigido
