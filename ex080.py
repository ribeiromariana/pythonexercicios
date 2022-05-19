num = []
for c in range(0, 5):
    n = int(input('Digite o número que quer adicionar: '))
    if c == 0 or n > num[len(num) - 1]:
        num.append(n)
        print('Número adicionado no final da lista.')
    else:
        posicao = 0
        while posicao != len(num):
            if n <= num[posicao]:
                num.insert(posicao, n)
                print(f'Número adicionado na posição {posicao} da lista.')
                break
            posicao += 1
print(f'Os números adicionados foram: {num}')
# Tive que ver o vídeo da solução para conseguir fazer o programa, acho que estava uns 30% certo, mas só depois de ver
# a solução que consegui.
    