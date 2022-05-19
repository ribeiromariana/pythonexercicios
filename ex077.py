palavras = ('Arroz', 'Oi', 'Pao', 'Rocha', 'Pena', 'Shampoo', 'Lindo', 'Branco', 'Preto', 'Rosa', 'Chega', 'Beleza')
cont = -1
for p in palavras:
    print(f'\n{p} tem as vogais: ', end='')
    letras = len(p) - 1
    while cont != letras:
        if p[letras] in 'AaEeIiOoUu':
            print(p[letras], end=' ')
        letras -= 1
