city = str(input('Digite o nome da sua cidade: ')).split()
print('Analizando se sua cidade começa com Santo...')
resultado = (city[0].upper() == 'SANTO')
if resultado == True:
    print('Sim, a sua cidade começa com Santo!!')
else:
    print('A sua cidade não começa com Santo! :(')
#Corrigido