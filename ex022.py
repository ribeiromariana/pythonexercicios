nome = input('Digite o seu nome completo: ').strip()
print(f'Nome com letras maiúsculas: {nome.upper()}. \nNome com letras minúsculas: {nome.lower()}.')
dividido = nome.split()
juntas = ''.join(dividido)
contando = nome.count(' ')
print(f'O nome completo tem {len(nome) - contando} letras.')
print(f'O 1º nome é {dividido[0]} e tem {len(dividido[0])} letras.')
#Corrigido
