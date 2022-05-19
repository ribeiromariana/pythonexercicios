from time import sleep
def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    if inicio > fim:
        if passo > 0:
            passo = -passo
        elif passo < 0:
            passo = +passo
        fim -= 1
    elif fim > inicio:
        fim += 1

    for c in range(inicio, fim, passo):
        print(c, end=', ')
        sleep(0.5)
    print('FIM')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Faça a sua contagem personalizada: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
