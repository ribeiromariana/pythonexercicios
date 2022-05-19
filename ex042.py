reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
result = 'NÃO PODERÃO'
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    result = 'PODEM'
print(f'\033[32mAs retas acima \033[31m{result}\033[32m formar um triângulo!')
if 'PODEM' in result:
    if reta1 == reta2 == reta3:
        tipo = '\033[35mEQUILÁTERO'
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        tipo = '\033[34mISÓSCELES'
    else:
        tipo = '\033[33mESCALENO'
    print(f'E o tipo do triângulo será {tipo}')
