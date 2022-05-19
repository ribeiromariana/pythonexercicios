nome_completo = str(input('Digite o seu nome completo: ')).title().strip().split()
print('estamos analizando o seu nome...')
print(f'O primeiro nome é: {nome_completo[0]}')
nomes = len(nome_completo) - 1
print(f'O último nome é: {nome_completo[nomes]}')
print('Prazer em te conhecer!')
#Corrigido