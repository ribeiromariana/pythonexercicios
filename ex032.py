from datetime import date
ano = int(input('Digite o ano que você quer analizar! (Se quiser analizar o ano atual, digite 0): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')
# Corrigido
