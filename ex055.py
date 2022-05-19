menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f'\033[33mDigite o {p}º peso: kg'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\033[mO \033[36mMENOR peso foi {menor}kg\033[m e o \033[31mMAIOR foi {maior}kg\033[m!')
