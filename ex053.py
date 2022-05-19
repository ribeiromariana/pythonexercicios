frase = str(input('Digite uma frase sem acentos: ')).upper()
junta = ''.join(frase.split())
letras = len(junta)
ult_letra = ''
frase2 = ''
for c in range(1, len(junta) + 1):
    letras = letras - 1
    ult_letra = junta[letras]
    frase2 = frase2 + ult_letra
if frase2 == junta:
    print(f'A frase \033[33m{frase}\033[32m É um palíndromo\033[m, pois ao contrário fica: {frase2.upper()}')
else:
    print(f'A frase \033[35m{frase} \033[31mNÃO é um palindromo\033[m, pois ao contrário ela fica: {frase2.upper()}')
