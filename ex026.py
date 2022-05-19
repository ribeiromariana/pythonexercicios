frase = str(input('Digite uma frase qualquer: ')).lower().strip()
print(frase)
As = frase.count('a')
print(f'A aparece {As} vezes.')
primeira = frase.find('a') + 1
print(f'A aparece pela PRIMEIRA vez na posição {primeira}.')
ultima = frase.rfind('a') + 1
print(f'A aparece pela ÚLTIMA vez na posição {ultima}.')
#Corrigido