from time import sleep
print('\033[34m-~* 10 Primeiros termos de uma PA *~-\033[m')
primeiro_t = int(input('\033[35mPrimeiro termo: '))
razao = int(input('\033[33mRazão: \033[m'))
prox_t = primeiro_t
termos = 1
while termos != 11:
    print(prox_t, end=' → ')
    termos += 1
    prox_t += razao
    sleep(0.5)
print('ACABOU')
pergunta = int(input('\033[36mVocê quer ver mais quantos termos? \033[m'))
quantidade_t = 10
while pergunta != 0:
    quantidade_t += pergunta
    prox_t = primeiro_t
    termos = 0
    while termos != quantidade_t:
        print(prox_t, end=' → ')
        termos += 1
        prox_t += razao
        sleep(0.3)
    print('ACABOU')
    pergunta = int(input('\033[36mVocê quer ver mais quantos termos? \033[m'))
print('\033[32mPrograma encerrado.')
