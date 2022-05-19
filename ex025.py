nome = str(input('Digite o seu nome inteiro: ')).strip().upper().split()
print('Iremos verificar se seu nome tem SILVA...')
teste = 'SILVA' in nome
print(f'O seu nome tem Silva? {teste}')
#Corrigido