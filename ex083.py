expressao = [str(input('Digite uma expressão numérica (com parênteses): '))]
abrem = expressao[0].count('(')
fecham = expressao[0].count(')')
if abrem == fecham:
    print('\033[32mExpressão válida.')
else:
    print('\033[31mExpressão inválida.')
