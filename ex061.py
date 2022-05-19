primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termos = 0
prox_termo = primeiro_termo
while termos != 10:
    print(prox_termo, end=' → ')
    termos += 1
    prox_termo += razao
print('ACABOU')
