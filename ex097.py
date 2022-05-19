def escreva(texto):
    tam = len(texto) + 2
    print('¬' * tam)
    print(f' {texto}')
    print('¬' * tam)


escreva('Olá Familia!')
escreva('Mariana Ribeiro de Oliveira')
escreva('Quem leu isso é linda!')
msg = str(input('Digite o que você quiser: '))
escreva(msg)
