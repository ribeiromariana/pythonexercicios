sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while not sexo in 'MF':
    print('\033[31mValor errado. Tente novamente digitando M ou F.\033[m')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
print('\033[32mMuito obrigada por responder a nossa pesquisa!\033[m')
